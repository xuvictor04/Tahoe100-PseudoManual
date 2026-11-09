---
symbol: "FSBP"
type: "gene"
col: 15468
ensembl_id: "ENSG00000265817"
name: "fibrinogen silencer binding protein"
location: "8q22.1"
module: 71
arm: "+"
pooled_cpm: 8.75
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# FSBP

*fibrinogen silencer binding protein* — 8q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.90× (z +9.9, q 1e-20, up in 33 of 46 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM: 1.42× (z +5.2, q 2e-05, up in 11 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.483× (z -11.3, q 7e-27, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAD54B]] (+0.75, fdr 7e-06, ⚠ same locus), [[CEP152]] (+0.62, fdr 1e-05), [[BARD1]] (+0.61, fdr 1e-05), [[CTDSPL2]] (+0.61, fdr 1e-05); moves opposite to [[GRK4]] (-0.60, fdr 4e-05), [[LINC02646]] (-0.59, fdr 5e-05), [[ERICH1]] (-0.58, fdr 3e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15468.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.90×** | +9.9 | 1e-20 | 33/46 (NCI-H2347, HOP62, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.72×** | +8.4 | 1e-14 | 23/46 (LOX-IMVI, NCI-H2347, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.70×** | +8.2 | 3e-14 | 25/46 (HOP62, NCI-H2347, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.43×** | +5.3 | 2e-05 | 6/14 (NCI-H2347, HS-578T, …) | inconsistent across doses | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.42×** | +5.2 | 2e-05 | 11/44 (CFPAC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +5.1 | 3e-05 | 9/46 (PANC-1, KATO III, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.69×** | +4.2 | 0.002 | 11/40 (RPMI-7951, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +4.1 | 0.003 | 11/44 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.31×** | +3.9 | 0.006 | 5/19 (J82, NCI-H2347, …) | inconsistent across doses | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.26×** | +3.4 | 0.042 | 6/46 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.51×** | +3.3 | 0.042 | 4/45 (RKO, LOX-IMVI, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.24×** | +3.3 | 0.047 | 6/46 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.16× | +3.2 | 0.065 | 6/44 (RKO, HCT15, …) | rises with dose |  |
| [[Clotrimazole (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.070 | 4/44 (HT-29, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.083 | 6/46 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15468.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.483×** | -11.3 | 7e-27 | 29/45 (SW480, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.677×** | -5.8 | 1e-06 | 16/36 (NCI-H2030, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.803×** | -4.8 | 3e-04 | 17/45 (LS 180, CFPAC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.566×** | -4.6 | 5e-04 | 15/44 (PANC-1, SW1417, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.760×** | -4.0 | 0.006 | 14/44 (KATO III, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.767×** | -3.8 | 0.012 | 14/41 (COLO 205, NCI-H460, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.788×** | -3.5 | 0.036 | 4/47 (RKO, NCI-H460, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | 0.677× | -3.2 | 0.11 | 6/47 (Hs 766T, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.680× | -3.1 | 0.11 | 14/40 (LS 180, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[(S)-Crizotinib (drug)]] 5 µM |  | 0.813× | -3.1 | 0.11 | 5/45 (LOX-IMVI, NCI-H2347, …) | top dose only | position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.871× | -3.1 | 0.11 | 10/45 (Hs 766T, AN3 CA, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15468. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0497× (z -11.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 17.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 9.88 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0813× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 10.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.130× (z -10.0) |
| [[HT-29 (line)]] | alt | 5.66 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.109× (z -9.0) |
| [[KATO III (line)]] | alt | 10.1 | 0 | 1 | — | [[c-Kit-IN-1 (drug)]] 5 µM 0.0460× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 4.21 | 0 | 1 | — | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM 0.0459× (z -10.2) |
| [[LS 180 (line)]] | wt | 12.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -12.0) ⚠ cell-cycle shift, explains ~73% of this change |
| [[NCI-H1573 (line)]] | alt | 3.08 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0790× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.211× (z -8.8) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 5.58 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0826× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 8.61 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.228× (z -8.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 7.71 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.5 µM 0.0866× (z -8.6) |
| [[SW480 (line)]] | alt | 11.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.255× (z -10.1) |
| [[A-172 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15468), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD54B]] | +0.75 | +0.73 / +0.74 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[CEP152]] | +0.62 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[BARD1]] | +0.61 | +0.56 / +0.55 | both halves | 1e-05 | STRING 443 |
| [[CTDSPL2]] | +0.61 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[POLD3]] | +0.59 | +0.42 / +0.62 | both halves | 4e-05 | STRING 430 |
| [[SLF1]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[MNS1]] | +0.57 | +0.35 / +0.63 | both halves | 1e-04 |  |
| [[USP54]] | +0.55 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[MAP2K6]] | +0.55 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[PBK]] | +0.55 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[ATAD2]] | +0.55 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[CENPU]] | +0.55 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[UBE2T]] | +0.55 | +0.48 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRK4]] | -0.60 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[LINC02646]] | -0.59 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[ERICH1]] | -0.58 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[WDR81]] | -0.54 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[SLC23A3]] | -0.54 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[DENND6A-AS1]] | -0.53 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[ZNF432]] | -0.52 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[CAVIN4]] | -0.52 | -0.36 / -0.58 | both halves | 1e-04 |  |
| [[KLHL21]] | -0.52 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[SMIM12]] | -0.50 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[DNAH10]] | -0.50 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[NUP210L]] | -0.50 | -0.36 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.294). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.0, -50.3); signed map (-42.8, -40.3). **Vector** length 68.0, 10.4% of its response variance represented; |z| ≥ 3 in 980 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.6 | +1.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | +2.5 | +5.3 |
|  | [[NG25 (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +4.1 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +1.4 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.3 | +5.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.3 | +2.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.3 | +2.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.3 | +0.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.4 | -11.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.4 | -3.8 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | -2.3 | -3.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | fibrinogen silencer binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:94,378,377-94,436,952 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [O95073](https://www.uniprot.org/uniprotkb/O95073) (Fibrinogen silencer-binding protein):

> Transcriptional repressor that down-regulates the expression of the fibrinogen gamma chain. Represses transcription of GSK3B gene promoter via its interaction with APBA1.

**Summary**, from NCBI Gene [100861412](https://www.ncbi.nlm.nih.gov/gene/100861412):

> Enables identical protein binding activity. Predicted to be involved in DNA-templated transcription. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:43653](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43653) · Entrez [100861412](https://www.ncbi.nlm.nih.gov/gene/100861412) · UniProt [O95073](https://www.uniprot.org/uniprotkb/O95073) · Ensembl [ENSG00000265817](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000265817)

## Data

Gene col 15468: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15468); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15468, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15468]; `tensor/DDL_lfc|DDL_z.npy` [15468]; `embed/gene_vectors.npy` [15468]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15468 or target_col == 15468). Every well: [[FSBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FSBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
