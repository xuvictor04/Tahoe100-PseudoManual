---
symbol: "RPL7A"
type: "gene"
col: 7262
ensembl_id: "ENSG00000148303"
name: "ribosomal protein L7a"
location: "9q34.2"
module: 131
arm: "+"
pooled_cpm: 252.75
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# RPL7A

*ribosomal protein L7a* — 9q34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.69× (z +6.1, q 7e-07, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.45×; ⚠ cell-cycle shift, explains ~49% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.578× (z -6.3, q 2e-07, down in 42 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (HCT15 0.301×, SNU-1 0.343×, C-33 A 0.382×, RKO 0.417×, …).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS25]] (+0.95, fdr 7e-06), [[RPL8]] (+0.92, fdr 7e-06, ⚠ RPL8 in the vector space only through flagged drug-doses), [[RPL15]] (+0.92, fdr 7e-06), [[RPS10]] (+0.92, fdr 7e-06); moves opposite to [[MIS12]] (-0.65, fdr 1e-05).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7262.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.45×; ⚠ cell-cycle shift, explains ~49% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.69×** | +6.1 | 7e-07 | 48/49 (A549, LoVo, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.96×** | +4.8 | 5e-04 | 40/44 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.79×** | +4.7 | 5e-04 | 45/48 (SW 900, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +3.4 | 0.082 | 2/50 (NCI-H23, BT-474) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.3 | 0.094 | 40/47 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | 1.45× | +3.0 | 0.25 | 30/48 (NCI-H460, NCI-H1792, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7262.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (HCT15 0.301×, SNU-1 0.343×, C-33 A 0.382×, RKO 0.417×, …).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.578×** | -6.3 | 2e-07 | 42/48 (HCT15, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.674× | -3.2 | 0.40 | 43/48 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7262. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 277 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -9.9) |
| [[CHP-212 (line)]] | wt | 270 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -8.6) |
| [[HCT15 (line)]] | alt | 288 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -11.3) |
| [[LS 180 (line)]] | wt | 344 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 249 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +9.0) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H460 (line)]] | wt | 380 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -9.2) |
| [[RKO (line)]] | wt | 715 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -9.5) |
| [[SNU-1 (line)]] | wt | 351 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -10.1) |
| [[SW480 (line)]] | alt | 309 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -8.5) |
| [[A-172 (line)]] | wt | 155 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 178 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 246 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 304 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 282 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 232 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 329 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 232 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 261 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 176 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 298 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 233 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 267 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 338 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 313 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 325 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 258 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 315 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 278 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 393 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7262), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 23 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS25]] | +0.95 | +0.92 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL8]] ⚠ | +0.92 | +0.87 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL15]] | +0.92 | +0.89 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS10]] | +0.92 | +0.85 / +0.92 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS16]] ⚠ | +0.92 | +0.87 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL36A]] | +0.92 | +0.88 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL32]] | +0.92 | +0.84 / +0.91 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS23]] | +0.92 | +0.85 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS13]] ⚠ | +0.91 | +0.83 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS8]] | +0.91 | +0.85 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL13]] | +0.91 | +0.85 / +0.91 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL28]] | +0.91 | +0.86 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS5]] | +0.90 | +0.87 / +0.89 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS21]] | +0.90 | +0.80 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS24]] | +0.89 | +0.88 / +0.88 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIS12]] | -0.65 | -0.60 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.933). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-47.0, -27.6); signed map (-61.7, -3.6). **Vector** length 87.2, 50.9% of its response variance represented; |z| ≥ 3 in 383 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-2 modulates host translation machinery* (reactome, mean cos +0.88 to 12); *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.89 to 11); *Formation of the ternary complex, and subsequently, the 43S complex* (reactome, mean cos +0.89 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.5 | +1.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.5 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +1.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +0.8 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.3 | +1.0 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +1.8 | -0.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.7 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -7.6 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -7.4 | +4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.4 | -6.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | +0.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | +0.0 |
|  | [[Docetaxel (drug)]] 5 µM |  | -1.6 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L7a |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.2 — chr9:133,348,218-133,351,426 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SURF3, TRUP, L7A, eL8 |
| Gene groups (HGNC) | L ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P62424](https://www.uniprot.org/uniprotkb/P62424) (Large ribosomal subunit protein eL8):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6130](https://www.ncbi.nlm.nih.gov/gene/6130):

> Cytoplasmic ribosomes, organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L7AE family of ribosomal proteins. It can interact with a subclass of nuclear hormone receptors, including thyroid hormone receptor, and inhibit their ability to …

**Accessions** — [HGNC:10364](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10364) · Entrez [6130](https://www.ncbi.nlm.nih.gov/gene/6130) · UniProt [P62424](https://www.uniprot.org/uniprotkb/P62424) · Ensembl [ENSG00000148303](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148303)

## Data

Gene col 7262: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7262); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7262, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7262]; `tensor/DDL_lfc|DDL_z.npy` [7262]; `embed/gene_vectors.npy` [7262]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7262 or target_col == 7262). Every well: [[RPL7A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL7A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
