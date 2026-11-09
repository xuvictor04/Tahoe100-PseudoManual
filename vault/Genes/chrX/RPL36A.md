---
symbol: "RPL36A"
type: "gene"
col: 14267
ensembl_id: "ENSG00000241343"
name: "ribosomal protein L36a"
location: "Xq22.1"
module: 131
arm: "+"
pooled_cpm: 232.38
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# RPL36A

*ribosomal protein L36a* — Xq22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.30× (z +7.0, q 2e-09, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 5.61×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.577× (z -5.4, q 4e-05, down in 43 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (CHP-212 0.309×, HCT15 0.347×, SNU-1 0.348×, C-33 A 0.379×, …).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS10]] (+0.95, fdr 7e-06), [[RPS25]] (+0.94, fdr 7e-06), [[RPS29]] (+0.94, fdr 7e-06).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14267.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 5.61×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.30×** | +7.0 | 2e-09 | 49/49 (COLO 205, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.64×** | +6.5 | 2e-08 | 44/44 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +4.8 | 4e-04 | 42/45 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.92×** | +4.6 | 7e-04 | 45/48 (CFPAC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +4.1 | 0.006 | 44/47 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.60×** | +3.3 | 0.089 | 40/48 (NCI-H460, NCI-H1792, …) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 2.31× | +3.0 | 0.19 | 45/48 (AsPC-1, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14267.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (CHP-212 0.309×, HCT15 0.347×, SNU-1 0.348×, C-33 A 0.379×, …).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.577×** | -5.4 | 4e-05 | 43/48 (CHP-212, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14267. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 223 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -8.8) |
| [[CHP-212 (line)]] | wt | 181 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -9.1) |
| [[COLO 205 (line)]] | alt | 130 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.61× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 170 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -8.9) |
| [[LS 180 (line)]] | wt | 222 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -8.6) |
| [[RKO (line)]] | wt | 254 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -8.5) |
| [[SNU-1 (line)]] | wt | 185 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -8.9) |
| [[SW480 (line)]] | alt | 343 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -8.6) |
| [[A-172 (line)]] | wt | 73.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 226 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 201 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 236 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 166 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 173 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 167 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 186 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 198 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 131 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 249 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 166 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 265 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 307 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 307 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 356 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 228 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 350 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 258 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 218 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 293 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 335 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 363 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 261 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14267), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 23 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS10]] | +0.95 | +0.91 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 987 |
| [[RPS25]] | +0.94 | +0.91 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 995 |
| [[RPS29]] | +0.94 | +0.88 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL31]] | +0.94 | +0.89 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS13]] ⚠ | +0.94 | +0.90 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 996; ⚠ in the vector space only through flagged drug-doses |
| [[RPLP2]] | +0.94 | +0.89 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 995 |
| [[RPS8]] | +0.93 | +0.91 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 998 |
| [[RPL34]] | +0.93 | +0.89 / +0.91 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL9]] ⚠ | +0.93 | +0.89 / +0.91 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 997; ⚠ in the vector space only through flagged drug-doses |
| [[RPL13]] | +0.92 | +0.90 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 993 |
| [[RPL32]] | +0.92 | +0.89 / +0.91 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS21]] | +0.92 | +0.87 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL38]] | +0.92 | +0.84 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL23]] | +0.92 | +0.87 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 998 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.962). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-46.6, -27.2); signed map (-61.2, -3.4). **Vector** length 87.2, 51.2% of its response variance represented; |z| ≥ 3 in 420 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-2 modulates host translation machinery* (reactome, mean cos +0.89 to 12); *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.91 to 11); *Formation of the ternary complex, and subsequently, the 43S complex* (reactome, mean cos +0.91 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.9 | +0.4 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.5 | +0.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.5 | +0.6 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +2.2 | +0.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.5 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.5 | +7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.2 | +6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.3 | -5.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | -4.2 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | +0.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.0 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L36a |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.1 — chrX:101,390,824-101,396,155 (+) |
| Ensembl biotype | protein_coding |
| Also known as | L36A, eL42; previously RPL44 |
| Gene groups (HGNC) | L ribosomal proteins |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P83881](https://www.uniprot.org/uniprotkb/P83881) (Large ribosomal subunit protein eL42):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6173](https://www.ncbi.nlm.nih.gov/gene/6173):

> Cytoplasmic ribosomes, organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein, which shares sequence similarity with yeast ribosomal protein L44, belongs to the L44E (L36AE) family of ribosomal proteins. Although this gene has been referred to as ribosomal …

**Accessions** — [HGNC:10359](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10359) · Entrez [6173](https://www.ncbi.nlm.nih.gov/gene/6173) · UniProt [P83881](https://www.uniprot.org/uniprotkb/P83881) · Ensembl [ENSG00000241343](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241343)

## Data

Gene col 14267: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14267); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14267, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14267]; `tensor/DDL_lfc|DDL_z.npy` [14267]; `embed/gene_vectors.npy` [14267]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14267 or target_col == 14267). Every well: [[RPL36A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL36A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
