---
symbol: "SHKBP1"
type: "gene"
col: 8348
ensembl_id: "ENSG00000160410"
name: "SH3KBP1 binding protein 1"
location: "19q13.2"
module: 2
arm: "+"
pooled_cpm: 15.17
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# SHKBP1

*SH3KBP1 binding protein 1* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.81× (z +10.9, q 9e-25, up in 25 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.47× (z +7.0, q 3e-10, up in 26 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.691× (z -6.8, q 6e-09, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAMTA2]] (+0.59, fdr 2e-05), [[DDA1]] (+0.59, fdr 7e-06), [[SUDS3]] (+0.55, fdr 1e-05); moves opposite to [[SPCS1]] (-0.46, fdr 2e-05), [[NTS]] (-0.46, fdr 1e-04), [[THSD4-AS1]] (-0.44, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8348.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.81×** | +10.9 | 9e-25 | 25/36 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +9.0 | 9e-17 | 15/27 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +8.0 | 3e-13 | 6/48 (Panc 03.27, J82, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +7.2 | 1e-10 | 18/32 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +7.0 | 3e-10 | 26/47 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +5.2 | 2e-05 | 17/45 (A-172, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +4.9 | 6e-05 | 18/47 (J82, HOP62, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.37×** | +4.1 | 0.003 | 13/44 (RPMI-7951, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +4.0 | 0.004 | 13/42 (KATO III, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.004 | 9/47 (HOP62, LoVo, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.23×** | +3.8 | 0.007 | 10/43 (NCI-H1792, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | **1.23×** | +3.8 | 0.007 | 8/47 (A549, RKO, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.053 | 6/45 (NCI-H1792, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.26× | +3.0 | 0.10 | 3/45 (LOX-IMVI, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8348.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.691×** | -6.8 | 6e-09 | 26/47 (LOX-IMVI, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.730×** | -5.8 | 2e-06 | 20/47 (LOX-IMVI, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.747×** | -5.4 | 2e-05 | 19/46 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.779×** | -4.6 | 6e-04 | 17/47 (HT-29, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.823×** | -3.6 | 0.037 | 6/47 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.831×** | -3.4 | 0.063 | 12/48 (SW 1088, PANC-1, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.840× | -3.2 | 0.10 | 4/47 (A549, J82, …) | top dose only |  |
| [[Saquinavir (drug)]] 5 µM |  | 0.887× | -3.1 | 0.12 | 11/46 (HepG2/C3A, A498, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.845× | -3.1 | 0.12 | 9/47 (NCI-H2030, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8348. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 18.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.02× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 9.34 | 0 | 1 | — | [[Sulfatinib (drug)]] 5 µM 0.0662× (z -9.8) |
| [[J82 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.179× (z -11.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 13.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.33× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 12.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-423 (line)]] | alt | 11.0 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.173× (z -8.5) |
| [[A-172 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8348), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMTA2]] | +0.59 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[DDA1]] | +0.59 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[SUDS3]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[TRAPPC2]] | +0.54 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[SLC4A2]] | +0.54 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[TESK1]] | +0.53 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[USP35]] | +0.53 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[DMAP1]] | +0.53 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[TBKBP1]] | +0.53 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[MAPK3]] | +0.52 | +0.43 / +0.51 | both halves | 4e-05 |  |
| [[SPEG]] | +0.52 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[PIP4K2C]] | +0.52 | +0.56 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPCS1]] | -0.46 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[NTS]] | -0.46 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[THSD4-AS1]] | -0.44 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[SLC25A5]] | -0.44 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[IGIP]] | -0.43 | -0.38 / -0.50 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.436). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-10.5, -21.1); signed map (-28.3, -1.3). **Vector** length 68.2, 10.8% of its response variance represented; |z| ≥ 3 in 766 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +10.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.0 | +7.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +4.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.6 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +3.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +4.1 |
|  | [[Lopinavir (drug)]] 5 µM |  | +1.7 | +0.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -6.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.2 | -4.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.7 | -5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | -5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | -2.1 | -3.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.6 | -3.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -3.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 5 µM |  | -1.3 | -0.5 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.3 | -2.9 |
|  | [[Afatinib (drug)]] 0.05 µM |  | -1.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | SH3KBP1 binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:40,576,853-40,591,399 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PP203, Sb1 |
| Gene groups (HGNC) | WD repeat domain containing; BTB domain containing |
| Reactome | 4 pathways, smallest: CDC42 GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TBC3](https://www.uniprot.org/uniprotkb/Q8TBC3) (SH3KBP1-binding protein 1):

> Inhibits CBL-SH3KBP1 complex mediated down-regulation of EGFR signaling by sequestration of SH3KBP1. Binds to SH3KBP1 and prevents its interaction with CBL and inhibits translocation of SH3KBP1 to EGFR containing vesicles upon EGF stimulation.

**Summary**, from NCBI Gene [92799](https://www.ncbi.nlm.nih.gov/gene/92799):

> Enables identical protein binding activity. Predicted to be involved in positive regulation of epidermal growth factor receptor signaling pathway. Predicted to be located in lysosome and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19214](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19214) · Entrez [92799](https://www.ncbi.nlm.nih.gov/gene/92799) · UniProt [Q8TBC3](https://www.uniprot.org/uniprotkb/Q8TBC3) · Ensembl [ENSG00000160410](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160410)

## Data

Gene col 8348: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8348); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8348, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8348]; `tensor/DDL_lfc|DDL_z.npy` [8348]; `embed/gene_vectors.npy` [8348]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8348 or target_col == 8348). Every well: [[SHKBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHKBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
