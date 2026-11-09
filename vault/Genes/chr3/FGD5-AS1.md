---
symbol: "FGD5-AS1"
type: "gene"
col: 13479
ensembl_id: "ENSG00000225733"
name: "FGD5 antisense RNA 1"
location: "3p25.1"
module: 43
arm: "-"
pooled_cpm: 37.31
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 17
n_dd_up_clean: 4
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# FGD5-AS1

*FGD5 antisense RNA 1* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.54× (z +16.0, q 0e+00, up in 45 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.43× (z +6.4, q 2e-08, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.749× (z -5.2, q 1e-04, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MOB1A]] (+0.72, fdr 7e-06), [[CHRAC1]] (+0.68, fdr 7e-06), [[ADAT1]] (+0.68, fdr 7e-06); moves opposite to [[RBIS]] (-0.75, fdr 7e-06), [[RPL36]] (-0.73, fdr 7e-06), [[ATP5MJ]] (-0.72, fdr 7e-06).
> It sits in the **-** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[C5]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13479.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.54×** | +16.0 | 0e+00 | 45/45 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.44×** | +15.0 | 0e+00 | 39/40 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.21×** | +9.3 | 3e-18 | 37/42 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +6.4 | 2e-08 | 33/48 (NCI-H2347, BT-474, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +4.7 | 3e-04 | 27/47 (SW 900, BT-474, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.40×** | +4.2 | 0.002 | 27/48 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.38×** | +4.1 | 0.003 | 30/48 (A-172, HEC-1-A, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **1.32×** | +3.5 | 0.038 | 19/48 (A-172, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 1.28× | +3.1 | 0.11 | 16/48 (HOP62, A498, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 1.28× | +3.1 | 0.11 | 14/48 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.29× | +3.1 | 0.11 | 23/48 (NCI-H1792, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13479.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.749×** | -5.2 | 1e-04 | 27/47 (A-427, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.671×** | -5.1 | 1e-04 | 28/47 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.679×** | -4.9 | 2e-04 | 31/48 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.685×** | -4.8 | 2e-04 | 31/48 (HS-578T, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.687×** | -4.8 | 2e-04 | 29/48 (NCI-H1573, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.490×** | -4.7 | 2e-04 | 28/48 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.677×** | -4.7 | 2e-04 | 31/48 (A-427, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.693×** | -4.6 | 2e-04 | 30/48 (A-427, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.696×** | -4.6 | 3e-04 | 28/48 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.697×** | -4.6 | 3e-04 | 26/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.699×** | -4.5 | 3e-04 | 30/48 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.710×** | -4.4 | 6e-04 | 22/47 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.714×** | -4.1 | 0.002 | 23/48 (A-427, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.571×** | -3.7 | 0.008 | 20/48 (A-427, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.680×** | -3.5 | 0.018 | 19/48 (A498, C-33 A, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.761×** | -3.5 | 0.019 | 25/48 (HEC-1-A, A-427, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13479. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 39.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +10.8) | — |
| [[PANC-1 (line)]] | alt | 42.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +13.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.388× (z -9.1) |
| [[A-172 (line)]] | wt | 69.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.78× (z +12.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -9.3) |
| [[A-427 (line)]] | wt | 68.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -17.9) |
| [[HEC-1-A (line)]] | alt | 69.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.89× (z +13.5) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 39.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +11.2) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 39.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.94× (z +9.3) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 39.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.05× (z +13.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 25.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.26× (z +12.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 32.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.41× (z +9.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 35.3 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.107× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Roxadustat (drug)]] 0.05 µM 0.110× (z -8.6) |
| [[HOP62 (line)]] | alt | 45.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.02× (z +11.3) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 51.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 26.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.3× (z +15.1) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 26.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.29× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 47.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +11.5) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 59.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +12.4) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 37.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.17× (z +10.8) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 21.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +10.2) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 20.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.22× (z +8.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 10.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.00× (z +8.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 26.3 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0977× (z -9.0) ⚠ cell-cycle shift, explains ~5% of this change |
| [[HCT15 (line)]] | alt | 29.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.66× (z +8.9) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 24.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +9.1) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 39.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +9.3) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 42.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +9.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 32.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +11.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 32.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.21× (z +11.0) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 25.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 32.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +11.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 39.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +8.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 24.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0994× (z -13.0) ⚠ cell-cycle shift, explains ~10% of this change |
| [[A498 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13479), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*34 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB1A]] | +0.72 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[CHRAC1]] | +0.68 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[ADAT1]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[DARS2]] | +0.67 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[EIF4G2]] | +0.66 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[ZNF236]] | +0.66 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[TUG1]] | +0.66 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[PSME3]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ZMYND11]] | +0.65 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[SSU72]] | +0.65 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[HNRNPK]] | +0.65 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[OXCT1]] | +0.63 | +0.55 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*66 of its nearest partners move opposite, 12 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBIS]] | -0.75 | -0.60 / -0.74 | both halves | 7e-06 |  |
| [[RPL36]] | -0.73 | -0.69 / -0.68 | both halves | 7e-06 |  |
| [[ATP5MJ]] | -0.72 | -0.64 / -0.66 | both halves | 7e-06 |  |
| [[RPL18]] ⚠ | -0.72 | -0.63 / -0.65 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[LAMTOR5]] | -0.71 | -0.66 / -0.62 | both halves | 7e-06 |  |
| [[COMMD6]] | -0.71 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[RPS26]] | -0.70 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[SMIM26]] ⚠ | -0.69 | -0.62 / -0.63 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5ME]] | -0.68 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[SEC61G]] | -0.67 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[RPL35]] ⚠ | -0.66 | -0.55 / -0.62 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EDF1]] | -0.66 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[TOMM7]] | -0.66 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[RPS27]] | -0.66 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[RPL35A]] | -0.66 | -0.59 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C5]] | C | C5 activity raises FGD5-AS1's level | lines that do not express C5 (4) vs lines expressing it (46) | 1.78× lower at baseline in the lines without C5 | 0.097 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLSPN, PRDM6, TCF19; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **-** arm (projection on the module's main direction -0.591). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-43.2, -25.0); signed map (18.4, -33.4). **Vector** length 98.2, 26.3% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +15.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +16.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +9.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +3.6 | +2.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.5 | +1.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.0 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | +2.2 | +3.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.2 | +2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +4.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -2.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.4 | -1.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.2 | -4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | -3.0 | -2.4 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -3.0 | -1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | +0.5 |
|  | [[EX229 (drug)]] 0.5 µM |  | -2.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | FGD5 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p25.1 — chr3:14,920,347-14,948,424 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100505641](https://www.ncbi.nlm.nih.gov/gene/100505641):

> Biomarker of acute myocardial infarction. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:40410](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40410) · Entrez [100505641](https://www.ncbi.nlm.nih.gov/gene/100505641) · Ensembl [ENSG00000225733](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225733)

## Data

Gene col 13479: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13479); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13479, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13479]; `tensor/DDL_lfc|DDL_z.npy` [13479]; `embed/gene_vectors.npy` [13479]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13479 or target_col == 13479). Every well: [[FGD5-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGD5-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
