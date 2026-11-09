---
symbol: "EEF2K"
type: "gene"
col: 2352
ensembl_id: "ENSG00000103319"
name: "eukaryotic elongation factor 2 kinase"
location: "16p12.2"
module: 146
arm: "+"
pooled_cpm: 45.99
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 24
n_dd_up_clean: 12
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# EEF2K

*eukaryotic elongation factor 2 kinase* — 16p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 1.41× (z +8.0, q 8e-13, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.414× (z -28.6, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFP64]] (+0.63, fdr 9e-06), [[AGAP3]] (+0.61, fdr 7e-06), [[ANKRD16]] (+0.60, fdr 4e-05); moves opposite to [[CHMP1B]] (-0.56, fdr 1e-05), [[BACH1]] (-0.55, fdr 1e-05), [[STK38L]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ABL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2352.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +8.0 | 8e-13 | 34/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.26×** | +7.4 | 4e-11 | 27/48 (AsPC-1, NCI-H1792, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.34×** | +6.8 | 3e-09 | 35/48 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +5.9 | 5e-07 | 20/48 (NCI-H460, SW480, …) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 5 µM |  | **1.53×** | +5.1 | 4e-05 | 19/48 (KATO III, A549, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.50×** | +4.9 | 1e-04 | 20/48 (LoVo, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 5 µM |  | **1.48×** | +4.8 | 2e-04 | 15/48 (J82, A-172, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bentamapimod (drug)]] 5 µM |  | **1.48×** | +4.7 | 2e-04 | 14/48 (KATO III, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 0.5 µM |  | **1.32×** | +4.5 | 4e-04 | 14/48 (NCI-H460, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.22×** | +4.5 | 4e-04 | 15/48 (A-172, NCI-H460, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.30×** | +4.3 | 0.001 | 17/47 (A498, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.05 µM |  | 1.19× | +4.1 | 0.002 | 12/48 (KATO III, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.05 µM |  | **1.21×** | +4.1 | 0.002 | 14/48 (KATO III, SNU-1, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.19× | +4.0 | 0.003 | 12/48 (KATO III, AsPC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.9 | 0.003 | 16/48 (SW 900, NCI-H460, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 1.17× | +3.4 | 0.020 | 10/48 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | 1.17× | +3.4 | 0.021 | 13/47 (A-172, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2352.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.414×** | -28.6 | 0e+00 | 43/48 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.452×** | -17.6 | 0e+00 | 37/48 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.508×** | -15.6 | 0e+00 | 40/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.588×** | -12.2 | 3e-32 | 40/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.581×** | -12.0 | 4e-31 | 25/41 (SW48, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.600×** | -10.9 | 1e-25 | 30/45 (C32, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.634×** | -10.5 | 7e-24 | 34/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.636×** | -10.4 | 2e-23 | 29/47 (HCT15, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.640×** | -10.3 | 5e-23 | 36/48 (LS 180, HS-578T, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.651×** | -9.9 | 3e-21 | 35/48 (HS-578T, A498, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.651×** | -9.9 | 3e-21 | 33/48 (PANC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.666×** | -9.4 | 4e-19 | 35/48 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.468×** | -9.1 | 3e-18 | 33/49 (NCI-H460, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.686×** | -8.7 | 2e-16 | 32/48 (HS-578T, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.701×** | -8.2 | 1e-14 | 30/47 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.713×** | -7.8 | 2e-13 | 29/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.721×** | -7.5 | 2e-12 | 28/48 (LS 180, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.732×** | -7.2 | 2e-11 | 28/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.838× | -5.7 | 3e-07 | 23/48 (A-172, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2352. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 40.6 | 1 (1 ⚠) | 11 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -18.8) |
| [[C32 (line)]] | wt | 50.3 | 0 | 8 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0617× (z -22.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.202× (z -19.7) |
| [[PANC-1 (line)]] | alt | 44.1 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -20.0) |
| [[A498 (line)]] | wt | 87.1 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -23.2) |
| [[HS-578T (line)]] | alt | 59.9 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -13.8) |
| [[HCT15 (line)]] | alt | 69.2 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0681× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.377× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 50.3 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.214× (z -14.7) |
| [[A-427 (line)]] | wt | 40.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.1000× (z -31.1) |
| [[A549 (line)]] | wt | 43.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -23.8) |
| [[KATO III (line)]] | alt | 51.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -13.1) |
| [[LoVo (line)]] | wt | 67.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -23.0) |
| [[RKO (line)]] | wt | 61.1 | 0 | 5 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0947× (z -20.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.243× (z -12.2) |
| [[SW1417 (line)]] | alt | 51.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -15.5) |
| [[LOX-IMVI (line)]] | wt | 29.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -14.1) |
| [[NCI-H2030 (line)]] | alt | 49.5 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.249× (z -20.0) |
| [[SK-MEL-2 (line)]] | alt | 52.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -13.1) |
| [[A-172 (line)]] | wt | 55.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.519× (z -9.6) |
| [[Hs 766T (line)]] | wt | 60.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -12.0) |
| [[LS 180 (line)]] | wt | 58.4 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.298× (z -11.3) |
| [[SW48 (line)]] | wt | 79.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.364× (z -8.7) |
| [[SW480 (line)]] | alt | 41.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -13.0) |
| [[H4 (line)]] | wt | 53.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HEC-1-A (line)]] | alt | 63.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.446× (z -9.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 20.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -14.5) |
| [[NCI-H1573 (line)]] | alt | 42.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 37.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -15.8) |
| [[Panc 03.27 (line)]] | alt | 30.9 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.476× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.366× (z -8.5) |
| [[SNU-423 (line)]] | alt | 47.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -11.3) |
| [[AN3 CA (line)]] | alt | 55.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -10.6) |
| [[BT-474 (line)]] | alt | 41.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -9.8) |
| [[C-33 A (line)]] | alt | 57.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -13.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 37.4 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.114× (z -8.8) |
| [[COLO 205 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HT-29 (line)]] | alt | 34.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -13.7) |
| [[NCI-H1792 (line)]] | alt | 38.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -13.7) |
| [[RPMI-7951 (line)]] | alt | 68.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -10.9) |
| [[SHP-77 (line)]] | alt | 44.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -10.8) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 72.5 | 0 | 1 | — | [[Lopinavir (drug)]] 0.05 µM 0.0626× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 55.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2352), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFP64]] | +0.63 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[AGAP3]] | +0.61 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[ANKRD16]] | +0.60 | +0.41 / +0.69 | both halves | 4e-05 |  |
| [[NOD1]] | +0.60 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[MMS19]] | +0.60 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[TADA1]] | +0.59 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[GATA4]] | +0.58 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[NT5DC3]] | +0.58 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[FLVCR1]] | +0.58 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[ZYG11A]] | +0.57 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[MLLT10]] | +0.57 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[HDHD5]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHMP1B]] | -0.56 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[BACH1]] | -0.55 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[STK38L]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[CARD6]] | -0.53 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[ZNF655]] | -0.53 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[CDKN2B]] | -0.52 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[PNRC2]] | -0.52 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[DDX5]] | -0.51 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[SSUH2]] | -0.50 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[TBILA]] | -0.50 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[SCAT1]] | -0.50 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[DHRS12]] | -0.50 | -0.45 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABL1]] | B | ABL1 activity lowers EEF2K's level | compounds that target ABL1: 3 of 6 raise it (Flumatinib, Ponatinib, Radotinib) | 50% of the class's compounds vs 2.2% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[PPARGC1B]] | C | PPARGC1B activity raises EEF2K's level | lines that do not express PPARGC1B (3) vs lines expressing it (47) | 1.70× lower at baseline in the lines without PPARGC1B | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, SPDL1, ARHGAP10; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **+** arm (projection on the module's main direction 0.631). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-6.7, -6.6); signed map (-40.5, 1.5). **Vector** length 112, 31.5% of its response variance represented; |z| ≥ 3 in 1,389 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +7.5 | +7.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.5 | +8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.7 | +5.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +4.2 | +6.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +2.1 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +4.1 | +4.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +3.9 | +5.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.8 | -10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.8 | -12.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | -4.7 | -10.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.4 | -5.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -7.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -4.3 | -2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.8 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic elongation factor 2 kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.2 — chr16:22,206,278-22,288,738 (+) |
| Ensembl biotype | protein_coding |
| Also known as | eEF-2K, CaMKIII |
| Gene groups (HGNC) | Alpha kinases |
| Reactome | 2 pathways, smallest: mTORC1-mediated signalling; MTOR signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [O00418](https://www.uniprot.org/uniprotkb/O00418) (Eukaryotic elongation factor 2 kinase):

> Threonine kinase that regulates protein synthesis by controlling the rate of peptide chain elongation. Upon activation by a variety of upstream kinases including AMPK or TRPM7, phosphorylates the elongation factor EEF2 at a single site, renders it unable to bind ribosomes and thus inactive. In turn, the rate of protein synthesis is reduced.

**Summary**, from NCBI Gene [29904](https://www.ncbi.nlm.nih.gov/gene/29904):

> This gene encodes a highly conserved protein kinase in the calmodulin-mediated signaling pathway that links activation of cell surface receptors to cell division. This kinase is involved in the regulation of protein synthesis. It phosphorylates eukaryotic elongation factor 2 (EEF2) and thus inhibits the EEF2 function. The activity of this kinase is increased in many cancers and may be a valid target for anti-cancer treatment. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:24615](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24615) · Entrez [29904](https://www.ncbi.nlm.nih.gov/gene/29904) · UniProt [O00418](https://www.uniprot.org/uniprotkb/O00418) · Ensembl [ENSG00000103319](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103319)

## Data

Gene col 2352: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2352); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2352, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2352]; `tensor/DDL_lfc|DDL_z.npy` [2352]; `embed/gene_vectors.npy` [2352]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2352 or target_col == 2352). Every well: [[EEF2K — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EEF2K.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
