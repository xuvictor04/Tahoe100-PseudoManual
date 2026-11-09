---
symbol: "CORO2A"
type: "gene"
col: 2806
ensembl_id: "ENSG00000106789"
name: "coronin 2A"
location: "9q22.33"
module: 31
arm: "+"
pooled_cpm: 27.8
n_lines_expressing: 47
n_dd_up: 10
n_dd_down: 32
n_dd_up_clean: 10
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 27
direction_downstream: 1
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# CORO2A

*coronin 2A* — 9q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.21× (z +14.2, q 6e-43, up in 35 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.392× (z -23.7, q 0e+00, down in 34 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPTLC2]] (+0.71, fdr 7e-06), [[P2RY2]] (+0.70, fdr 7e-06), [[AGPAT2]] (+0.67, fdr 1e-05); moves opposite to [[ZNF280D]] (-0.57, fdr 2e-05), [[ARMCX5-GPRASP2]] (-0.57, fdr 5e-05), [[DDX6]] (-0.57, fdr 8e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[PCDH1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PACSIN2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2806.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.21×** | +14.2 | 6e-43 | 35/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.06×** | +12.9 | 1e-35 | 36/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.87×** | +11.2 | 1e-26 | 36/44 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.86×** | +11.1 | 1e-26 | 36/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +9.9 | 5e-21 | 24/45 (RKO, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +8.6 | 8e-16 | 22/43 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +7.0 | 3e-10 | 25/43 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +6.3 | 2e-08 | 19/44 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.91×** | +6.0 | 1e-07 | 23/45 (MIA PaCa-2, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.022 | 12/44 (NCI-H1573, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2806.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.392×** | -23.7 | 0e+00 | 34/44 (AsPC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.276×** | -23.0 | 0e+00 | 41/45 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.342×** | -19.2 | 0e+00 | 33/43 (A-172, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.353×** | -18.6 | 0e+00 | 36/43 (HT-29, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.356×** | -17.7 | 0e+00 | 36/45 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.379×** | -17.3 | 0e+00 | 37/44 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.453×** | -14.2 | 1e-43 | 35/45 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.479×** | -13.2 | 1e-37 | 35/44 (BT-474, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.524×** | -11.1 | 7e-27 | 30/41 (BT-474, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.565×** | -9.4 | 2e-19 | 20/32 (LS 180, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.379×** | -9.1 | 6e-18 | 28/45 (Panc 03.27, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.624×** | -8.4 | 2e-15 | 26/44 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.636×** | -8.1 | 3e-14 | 30/44 (Panc 03.27, CFPAC-1, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.665×** | -7.3 | 1e-11 | 24/44 (Panc 03.27, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.667×** | -7.2 | 2e-11 | 25/45 (SNU-1, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.765×** | -6.8 | 5e-10 | 22/45 (Hs 766T, Panc 03.27, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.685×** | -6.4 | 5e-09 | 21/44 (Panc 03.27, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.505×** | -6.4 | 5e-09 | 20/41 (LS 180, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.715×** | -6.0 | 6e-08 | 19/45 (BT-474, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2806. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 54.7 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -20.0) |
| [[HT-29 (line)]] | alt | 76.1 | 0 | 10 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0872× (z -22.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.191× (z -21.5) |
| [[LS 180 (line)]] | wt | 40.6 | 1 | 9 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.11× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.103× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.320× (z -14.0) |
| [[Panc 03.27 (line)]] | alt | 75.3 | 0 | 9 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0887× (z -13.2) |
| [[A-172 (line)]] | wt | 62.7 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -19.6) |
| [[BT-474 (line)]] | alt | 32.5 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0781× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.189× (z -15.6) |
| [[Hs 766T (line)]] | wt | 121 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0898× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.120× (z -13.1) |
| [[COLO 205 (line)]] | alt | 52.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -16.4) |
| [[HOP62 (line)]] | alt | 24.2 | 0 | 6 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.162× (z -13.1) |
| [[J82 (line)]] | alt | 41.5 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0704× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.241× (z -15.1) |
| [[SW480 (line)]] | alt | 20.3 | 3 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.08× (z +9.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.245× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 40.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -25.9) |
| [[CFPAC-1 (line)]] | alt | 49.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -13.9) |
| [[HEC-1-A (line)]] | alt | 25.0 | 3 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +15.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.314× (z -8.9) |
| [[KATO III (line)]] | alt | 55.2 | 0 | 5 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.203× (z -13.4) |
| [[PANC-1 (line)]] | alt | 7.16 | 3 | 2 | [[Belinostat (drug)]] 5 µM 4.89× (z +9.2) | [[Digitoxin (drug)]] 0.5 µM 0.139× (z -11.4) |
| [[SW1417 (line)]] | alt | 56.1 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.268× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.400× (z -13.1) |
| [[NCI-H1573 (line)]] | alt | 12.3 | 2 | 2 | [[Betamethasone dipropionate (drug)]] 5 µM 8.04× (z +9.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 10.9 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.0867× (z -11.7) |
| [[NCI-H2347 (line)]] | alt | 30.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -11.4) |
| [[A549 (line)]] | wt | 12.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 19.2 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.169× (z -11.1) |
| [[RKO (line)]] | wt | 14.2 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.69× (z +9.8) | [[Harringtonine (drug)]] 5 µM 0.159× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 7.17 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.35× (z +10.0) | — |
| [[SK-MEL-2 (line)]] | alt | 11.4 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0976× (z -9.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.249× (z -8.7) |
| [[A498 (line)]] | wt | 28.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -9.7) |
| [[AN3 CA (line)]] | alt | 26.2 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 0.5 µM 0.0916× (z -8.9) |
| [[H4 (line)]] | wt | 10.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0549× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 29.8 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.128× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0835× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 7.62 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.125× (z -9.5) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -9.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 22.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.149× (z -8.5) |
| [[SW 900 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.176× (z -9.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -9.2) |
| [[A-427 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.20 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.93 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2806), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTLC2]] | +0.71 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[P2RY2]] | +0.70 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[AGPAT2]] | +0.67 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[LPCAT4]] | +0.63 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[CYTH1]] | +0.63 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[SLC66A2]] | +0.63 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[FKBP1B]] | +0.62 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[CLMN]] | +0.61 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[TMEM92]] | +0.61 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[MMP15]] | +0.61 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[SLC45A4]] | +0.60 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[PRSS8]] | +0.60 | +0.56 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF280D]] | -0.57 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[ARMCX5-GPRASP2]] | -0.57 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[DDX6]] | -0.57 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[TIA1]] | -0.56 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[MTHFSD]] | -0.55 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[TXNRD2]] | -0.55 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[AHI1-DT]] | -0.55 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[CASD1]] | -0.55 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[CARD8]] | -0.54 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[MFF-DT]] | -0.53 | -0.49 / -0.21 | both halves | 6e-04 |  |
| [[SUCLG2-DT]] | -0.53 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[DCAF8]] | -0.53 | -0.35 / -0.42 | both halves | 1e-04 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 27, C 0. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDH1]] | B | PCDH1 activity raises CORO2A's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.39× lower at baseline in the lines without PCDH1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[P2RY2]] | B | P2RY2 activity raises CORO2A's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 2.37× lower at baseline in the lines without P2RY2 | 0.004 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[TMEM92]] | B | TMEM92 activity strengthens CORO2A's drug response | lines that do not express TMEM92 (20) vs lines expressing it (25) | the lines without TMEM92 respond 0.65× as strongly (z diff +1.56); strongest at Homoharringtonine 0.5 µM: 0.57x vs 0.27x (z diff +4.4) | 0.006 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10; target measured in part of the lines; artifact flags |
| [[C6orf132]] | B | C6orf132 activity raises CORO2A's level | lines that do not express C6orf132 (27) vs lines expressing it (23) | 2.57× lower at baseline in the lines without C6orf132 | 0.006 | ⚠ within organs, on part of the lines; also absent: PCSK9, RNF223, CDH1 |
| [[PROSER2]] | B | PROSER2 activity raises CORO2A's level | lines that do not express PROSER2 (14) vs lines expressing it (36) | 2.37× lower at baseline in the lines without PROSER2 | 0.009 | ⚠ within organs, on part of the lines; also absent: BIK, EPS8L2, SERPINB9P1; maybe low, not absent |
| [[PKP2]] | B | PKP2 activity strengthens CORO2A's drug response | lines that do not express PKP2 (14) vs lines expressing it (31) | the lines without PKP2 respond 0.58× as strongly (z diff +1.92); strongest at Ouabain (Octahydrate) 0.5 µM: 0.68x vs 0.37x (z diff +3.8) | 0.012 | ⚠ within organs, on part of the lines; also absent: EPHA2-AS1, EPS8L2, OCLN; target measured in part of the lines; artifact flags |
| [[VSIR]] | B | VSIR activity raises CORO2A's level | lines that do not express VSIR (14) vs lines expressing it (36) | 1.97× lower at baseline in the lines without VSIR | 0.013 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |
| [[TTC9]] | B | TTC9 activity raises CORO2A's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 1.99× lower at baseline in the lines without TTC9 | 0.014 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises CORO2A's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 2.24× lower at baseline in the lines without TMPRSS4 | 0.024 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[GSDMC]] | B | GSDMC activity raises CORO2A's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 1.96× lower at baseline in the lines without GSDMC | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1 |
| [[PTK2B]] | B | PTK2B activity raises CORO2A's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 2.53× lower at baseline in the lines without PTK2B | 0.028 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[P2RY6]] | B | P2RY6 activity raises CORO2A's level | lines that do not express P2RY6 (29) vs lines expressing it (21) | 1.35× lower at baseline in the lines without P2RY6 | 0.035 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, FGG |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PACSIN2]] | C | CORO2A activity lowers PACSIN2's level | lines that do not express CORO2A (3) vs lines expressing it (47) | 1.84× higher at baseline in the lines without CORO2A | 0.065 | ⚠ few lines (3 vs 47); across organs; also absent: SLC4A11, NUDT7, SCAMP5; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.592). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.7, 4.3); signed map (-20.8, 34.6). **Vector** length 95.0, 23.9% of its response variance represented; |z| ≥ 3 in 1,446 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.4 | +11.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +14.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.0 | +12.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.5 | +7.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.5 | +11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +9.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +6.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | -0.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.7 | +1.2 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.5 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.1 | -19.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.1 | -17.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.3 | -6.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.9 | -14.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.2 | -23.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.1 | -1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -7.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.3 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | coronin 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.33 — chr9:98,120,975-98,192,637 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IR10, WDR2 |
| Gene groups (HGNC) | WD repeat domain containing; Coronins |
| Matched by | ensembl_id |

UniProt [Q92828](https://www.uniprot.org/uniprotkb/Q92828) carries no function annotation.

**Summary**, from NCBI Gene [7464](https://www.ncbi.nlm.nih.gov/gene/7464):

> This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. This protein contains 5 WD repeats, and has a structural similarity with …

**Accessions** — [HGNC:2255](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2255) · Entrez [7464](https://www.ncbi.nlm.nih.gov/gene/7464) · UniProt [Q92828](https://www.uniprot.org/uniprotkb/Q92828) · Ensembl [ENSG00000106789](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106789)

## Data

Gene col 2806: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2806); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2806, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2806]; `tensor/DDL_lfc|DDL_z.npy` [2806]; `embed/gene_vectors.npy` [2806]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2806 or target_col == 2806). Every well: [[CORO2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CORO2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
