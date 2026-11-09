---
symbol: "RPS14"
type: "gene"
col: 8965
ensembl_id: "ENSG00000164587"
name: "ribosomal protein S14"
location: "5q33.1"
module: 43
arm: "+"
pooled_cpm: 245.42
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPS14

*ribosomal protein S14* — 5q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.69× (z +5.3, q 7e-05, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.417× (z -7.5, q 3e-11, down in 48 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 14 lines (SNU-1 0.190×, A-427 0.246×, NCI-H23 0.265×, CHP-212 0.252×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.165×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL31]] (+0.96, fdr 7e-06), [[RPL13]] (+0.96, fdr 7e-06), [[RPL26]] (+0.95, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8965.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.69×** | +5.3 | 7e-05 | 48/49 (C-33 A, NCI-H1792, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.93×** | +4.1 | 0.014 | 45/48 (Panc 03.27, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.95×** | +3.8 | 0.022 | 40/44 (NCI-H1792, NCI-H460, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +3.4 | 0.083 | 40/47 (CFPAC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | 1.74× | +3.2 | 0.17 | 35/45 (SNU-423, C-33 A, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | 1.66× | +3.1 | 0.17 | 36/48 (NCI-H460, NCI-H1573, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8965.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 14 lines (SNU-1 0.190×, A-427 0.246×, NCI-H23 0.265×, CHP-212 0.252×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.165×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.417×** | -7.5 | 3e-11 | 48/48 (SNU-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.572× | -3.4 | 0.20 | 38/48 (A-427, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8965. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 273 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -11.0) |
| [[C-33 A (line)]] | alt | 216 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -10.1) |
| [[CHP-212 (line)]] | wt | 229 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -10.4) |
| [[H4 (line)]] | wt | 195 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -9.3) |
| [[HT-29 (line)]] | alt | 242 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -9.4) |
| [[LoVo (line)]] | wt | 490 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 268 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -8.6) |
| [[LS 180 (line)]] | wt | 280 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 237 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 221 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 319 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 304 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -9.2) |
| [[RKO (line)]] | wt | 254 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -9.4) |
| [[SNU-1 (line)]] | wt | 244 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -12.9) |
| [[SW48 (line)]] | wt | 324 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -9.0) |
| [[SW480 (line)]] | alt | 262 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -9.7) |
| [[A-172 (line)]] | wt | 166 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 214 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 260 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 328 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 325 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 284 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 234 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 230 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 218 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 210 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 303 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 297 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 253 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8965), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 22 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL31]] | +0.96 | +0.93 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL13]] | +0.96 | +0.95 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL26]] | +0.95 | +0.93 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL35A]] | +0.95 | +0.91 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL17]] | +0.95 | +0.91 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 997 |
| [[RPL34]] | +0.95 | +0.92 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL35]] ⚠ | +0.95 | +0.91 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL23]] | +0.95 | +0.89 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS8]] | +0.94 | +0.89 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL9]] ⚠ | +0.94 | +0.88 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL19]] | +0.94 | +0.88 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL27]] | +0.93 | +0.91 / +0.92 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS27]] | +0.93 | +0.87 / +0.96 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS10]] | +0.92 | +0.85 / +0.93 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.959). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.5, -27.3); signed map (-60.1, -4.1). **Vector** length 90.4, 61.5% of its response variance represented; |z| ≥ 3 in 364 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.87 to 34); *MYC targets v1* (hallmark, mean cos +0.65 to 17); *oxidative phosphorylation* (hallmark, mean cos +0.70 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +0.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +1.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.7 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +0.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +0.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.3 | +0.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.0 | +1.3 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.0 | +0.7 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +2.0 | +0.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -7.9 | +5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -7.5 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -7.1 | +3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.4 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.1 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | +1.7 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -1.5 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.1 — chr5:150,442,635-150,449,739 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EMTB, S14, uS11 |
| Gene groups (HGNC) | S ribosomal proteins |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 52 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P62263](https://www.uniprot.org/uniprotkb/P62263) (Small ribosomal subunit protein uS11):

> Component of the small ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and …

**Summary**, from NCBI Gene [6208](https://www.ncbi.nlm.nih.gov/gene/6208):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 40S subunit. The protein belongs to the S11P family of ribosomal proteins. It is located in the cytoplasm. Transcript variants utilizing alternative transcription initiation sites have been described in the …

**Accessions** — [HGNC:10387](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10387) · Entrez [6208](https://www.ncbi.nlm.nih.gov/gene/6208) · UniProt [P62263](https://www.uniprot.org/uniprotkb/P62263) · Ensembl [ENSG00000164587](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164587)

## Data

Gene col 8965: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8965); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8965, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8965]; `tensor/DDL_lfc|DDL_z.npy` [8965]; `embed/gene_vectors.npy` [8965]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8965 or target_col == 8965). Every well: [[RPS14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
