---
symbol: "CCZ1B"
type: "gene"
col: 7105
ensembl_id: "ENSG00000146574"
name: "CCZ1B vacuolar protein trafficking and biogenesis associated"
location: "7p22.1"
module: 30
arm: "+"
pooled_cpm: 21.44
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 10
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# CCZ1B

*CCZ1B vacuolar protein trafficking and biogenesis associated* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.00× (z +6.0, q 1e-06, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.577× (z -9.1, q 3e-17, down in 31 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.740× (z -4.8, q 3e-04, down in 21 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCZ1]] (+0.97, fdr 7e-06), [[SDHAP2]] (+0.74, fdr 7e-06), [[KLHDC10]] (+0.72, fdr 7e-06); moves opposite to [[HNRNPA2B1]] (-0.71, fdr 7e-06), [[PPP1R10]] (-0.69, fdr 7e-06), [[HNRNPK]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 030]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7105.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.00×** | +6.0 | 1e-06 | 25/48 (KATO III, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +5.1 | 9e-05 | 23/47 (BT-474, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +4.7 | 4e-04 | 15/48 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +4.1 | 0.005 | 18/48 (KATO III, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +4.1 | 0.005 | 19/47 (NCI-H2030, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +3.1 | 0.16 | 12/48 (NCI-H23, H4, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +3.1 | 0.17 | 11/48 (SW1417, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7105.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.577×** | -9.1 | 3e-17 | 31/41 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.685×** | -6.1 | 4e-07 | 19/35 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.740×** | -4.8 | 3e-04 | 21/48 (H4, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.820×** | -4.7 | 4e-04 | 21/47 (LoVo, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.763×** | -4.5 | 8e-04 | 20/48 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -4.1 | 0.004 | 3/48 (NCI-H1573, AN3 CA, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.785×** | -4.0 | 0.004 | 17/48 (PANC-1, SW48, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.790×** | -3.9 | 0.006 | 20/47 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.807×** | -3.6 | 0.023 | 13/48 (SW 1088, HS-578T, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.809×** | -3.5 | 0.024 | 14/48 (BT-474, MIA PaCa-2, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.811×** | -3.5 | 0.026 | 12/48 (A498, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7105. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 34.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -10.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 21.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -10.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[KATO III (line)]] | alt | 33.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -12.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 24.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -13.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 17.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.223× (z -8.8) |
| [[C32 (line)]] | wt | 14.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -8.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[Hs 766T (line)]] | wt | 17.5 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.158× (z -11.1) |
| [[J82 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 27.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -14.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H460 (line)]] | wt | 18.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -17.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[RPMI-7951 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -9.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 37.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -10.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 34.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0924× (z -13.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7105), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCZ1]] | +0.97 | +0.94 / +0.94 | both halves | 7e-06 | pathway: RAB GEFs exchange GTP for GDP on RABs; STRING 968 |
| [[SDHAP2]] | +0.74 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[KLHDC10]] | +0.72 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[LCMT1]] | +0.72 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[CRYZL1]] | +0.71 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[MALSU1]] | +0.71 | +0.76 / +0.56 | both halves | 1e-05 |  |
| [[SDHAP1]] | +0.70 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[MMS19]] | +0.70 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[FAM193B]] | +0.68 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[GTF2H2B]] | +0.68 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[NCK1]] | +0.68 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[CDK5RAP1]] | +0.68 | +0.61 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPA2B1]] | -0.71 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[PPP1R10]] | -0.69 | -0.70 / -0.65 | both halves | 7e-06 |  |
| [[HNRNPK]] | -0.66 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[MTNR1A]] | -0.65 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[THOC6]] | -0.65 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[RNF32-AS1]] | -0.64 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[LINC00641]] | -0.64 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[ITPR2-AS1]] | -0.64 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[DDX5]] | -0.62 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[MYH15]] | -0.61 | -0.67 / -0.49 | both halves | 1e-05 |  |
| [[CELSR3]] | -0.61 | -0.67 / -0.48 | both halves | 2e-05 |  |
| [[KRT8P12]] | -0.61 | -0.61 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.768). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-0.2, -14.0); signed map (-37.3, 0.4). **Vector** length 80.2, 15.0% of its response variance represented; |z| ≥ 3 in 808 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +3.7 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.5 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.6 | +3.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.5 | +6.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +4.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.5 | -4.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.2 | -4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.1 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.9 | -3.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.1 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -2.4 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -2.0 | -1.5 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -2.0 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | CCZ1B vacuolar protein trafficking and biogenesis associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.1 — chr7:6,794,134-6,826,770 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP586I1023, H_NH0577018.2, MGC19819; previously C7orf28B |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

UniProt [P86790](https://www.uniprot.org/uniprotkb/P86790) carries no function annotation.

**Summary**, from NCBI Gene [221960](https://www.ncbi.nlm.nih.gov/gene/221960):

> Enables guanyl-nucleotide exchange factor activity. Predicted to be involved in vacuolar transport and vesicle-mediated transport. Located in late endosome. Part of Mon1-Ccz1 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21717](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21717) · Entrez [221960](https://www.ncbi.nlm.nih.gov/gene/221960) · UniProt [P86790](https://www.uniprot.org/uniprotkb/P86790) · Ensembl [ENSG00000146574](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146574)

## Data

Gene col 7105: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7105); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7105, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7105]; `tensor/DDL_lfc|DDL_z.npy` [7105]; `embed/gene_vectors.npy` [7105]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7105 or target_col == 7105). Every well: [[CCZ1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCZ1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
