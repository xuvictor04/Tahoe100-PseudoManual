---
symbol: "PTCH1"
type: "gene"
col: 11753
ensembl_id: "ENSG00000185920"
name: "patched 1"
location: "9q22.32"
module: 79
arm: "+"
pooled_cpm: 30.07
n_lines_expressing: 48
n_dd_up: 9
n_dd_down: 47
n_dd_up_clean: 9
n_dd_down_clean: 35
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# PTCH1

*patched 1* — 9q22.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.81× (z +22.6, q 0e+00, up in 38 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 47 drug-doses (12 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.398× (z -14.2, q 4e-43, down in 42 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNOT6L]] (+0.61, fdr 1e-05), [[TSHZ1]] (+0.60, fdr 3e-05), [[PAX6]] (+0.59, fdr 4e-05); moves opposite to [[ACOT9]] (-0.53, fdr 3e-05), [[CPLANE1]] (-0.51, fdr 2e-05), [[TRIP4]] (-0.51, fdr 3e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PAX6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11753.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.81×** | +22.6 | 0e+00 | 38/45 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +7.0 | 1e-09 | 30/45 (A-172, J82, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +5.2 | 4e-05 | 21/45 (A498, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +4.8 | 2e-04 | 20/46 (A-172, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.81×** | +4.8 | 2e-04 | 20/46 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.049 | 4/46 (SW480, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.080 | 20/45 (SW48, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ritonavir (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.093 | 9/46 (A498, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Tofacitinib (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.098 | 12/46 (NCI-H1792, LoVo, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.22× | +3.1 | 0.11 | 14/46 (NCI-H2347, A549, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.15× | +3.1 | 0.11 | 12/46 (SW1417, PANC-1, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 47 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11753.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.398×** | -14.2 | 4e-43 | 42/45 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.462×** | -11.9 | 4e-30 | 32/42 (SNU-1, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.452×** | -11.8 | 1e-29 | 35/46 (AN3 CA, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.480×** | -11.3 | 2e-27 | 32/46 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.482×** | -10.8 | 4e-25 | 27/35 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.498×** | -10.8 | 6e-25 | 40/46 (LS 180, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.617×** | -10.5 | 6e-24 | 31/46 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.530×** | -9.0 | 1e-17 | 25/38 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.496×** | -8.9 | 2e-17 | 34/46 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.573×** | -8.2 | 1e-14 | 31/42 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.592×** | -8.1 | 3e-14 | 30/45 (HepG2/C3A, COLO 205, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.584×** | -8.0 | 8e-14 | 34/45 (LS 180, COLO 205, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.571×** | -7.9 | 1e-13 | 32/46 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.706×** | -7.5 | 2e-12 | 33/46 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.601×** | -7.5 | 2e-12 | 32/45 (H4, LS 180, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.631×** | -7.1 | 5e-11 | 29/45 (LS 180, COLO 205, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.643×** | -6.8 | 4e-10 | 26/46 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.450×** | -6.4 | 4e-09 | 26/43 (A498, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.464×** | -6.2 | 2e-08 | 27/46 (SW480, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.680×** | -5.9 | 8e-08 | 27/46 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.682×** | -5.9 | 1e-07 | 27/45 (LS 180, SNU-423, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.490×** | -5.8 | 2e-07 | 27/45 (PANC-1, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11753. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 82.0 | 0 | 13 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.199× (z -15.9) |
| [[LS 180 (line)]] | wt | 108 | 0 | 11 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.169× (z -13.6) |
| [[NCI-H1573 (line)]] | alt | 19.4 | 0 | 10 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0883× (z -14.4) |
| [[A498 (line)]] | wt | 16.6 | 1 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.189× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 24.1 | 1 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +11.4) | [[Harringtonine (drug)]] 5 µM 0.200× (z -12.7) |
| [[HT-29 (line)]] | alt | 33.2 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.317× (z -8.7) |
| [[SNU-1 (line)]] | wt | 85.6 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.266× (z -8.6) |
| [[H4 (line)]] | wt | 34.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -11.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 87.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0599× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.0719× (z -12.8) |
| [[C-33 A (line)]] | alt | 141 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -10.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 52.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 17.2 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.41× (z +15.8) | [[Ixazomib citrate (drug)]] 5 µM 0.293× (z -9.3) |
| [[HOP62 (line)]] | alt | 20.1 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.96× (z +15.5) | [[Harringtonine (drug)]] 5 µM 0.248× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 12.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.322× (z -9.5) |
| [[PANC-1 (line)]] | alt | 15.6 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -11.1) |
| [[SHP-77 (line)]] | alt | 36.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[venetoclax (drug)]] 5 µM 0.0799× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 9.20 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.39× (z +11.0) | [[Docetaxel (drug)]] 0.05 µM 0.152× (z -8.7) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 21.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +10.1) | [[Harringtonine (drug)]] 5 µM 0.0903× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 32.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 20.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -11.2) |
| [[SNU-423 (line)]] | alt | 29.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.77× (z +12.1) | [[Selinexor (drug)]] 5 µM 0.347× (z -9.4) |
| [[SW48 (line)]] | wt | 41.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.202× (z -9.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 17.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.56× (z +13.6) | — |
| [[A549 (line)]] | wt | 13.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.29× (z +12.9) | — |
| [[C32 (line)]] | wt | 28.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +11.4) | — |
| [[CFPAC-1 (line)]] | alt | 9.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +9.4) | — |
| [[COLO 205 (line)]] | alt | 38.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.214× (z -9.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 20.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -10.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 27.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +12.5) | — |
| [[J82 (line)]] | alt | 19.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +14.2) | — |
| [[KATO III (line)]] | alt | 24.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +11.3) | — |
| [[LoVo (line)]] | wt | 18.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.96× (z +15.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 13.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 13.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.233× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 18.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.27× (z +11.7) | — |
| [[RKO (line)]] | wt | 23.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.30× (z +12.2) | — |
| [[RPMI-7951 (line)]] | alt | 8.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.60× (z +9.9) | — |
| [[SK-MEL-2 (line)]] | alt | 32.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +8.8) | — |
| [[SW 900 (line)]] | alt | 18.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -11.6) |
| [[SW1417 (line)]] | alt | 104 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -9.6) |
| [[A-427 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.66 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.24 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11753), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNOT6L]] | +0.61 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[TSHZ1]] | +0.60 | +0.43 / +0.68 | both halves | 3e-05 |  |
| [[PAX6]] | +0.59 | +0.42 / +0.60 | both halves | 4e-05 | STRING 494 |
| [[SAP30-DT]] | +0.58 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[ZMYM2]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[NARF]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[MXI1]] | +0.56 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[KDM3A]] | +0.56 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[RNASET2]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[GMCL1]] | +0.54 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[FAM117B]] | +0.54 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[USP28]] | +0.54 | +0.49 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACOT9]] | -0.53 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[CPLANE1]] | -0.51 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[TRIP4]] | -0.51 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[PTPN21]] | -0.50 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[ATP9B]] | -0.50 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[FKTN]] | -0.50 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[TTC4]] | -0.49 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[RFFL]] | -0.49 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[RAD54L2]] | -0.49 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[PVR]] | -0.49 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[CC2D1B]] | -0.48 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[DNAH14]] | -0.48 | -0.37 / -0.51 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAX6]] | B | PAX6 activity raises PTCH1's level | lines that do not express PAX6 (30) vs lines expressing it (20) | 1.94× lower at baseline in the lines without PAX6 | 0.035 | ⚠ within organs, on part of the lines; also absent: LINC02643, WT1-AS, CHRDL1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.536). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.1, -21.8); signed map (-33.7, 23.1). **Vector** length 113, 30.9% of its response variance represented; |z| ≥ 3 in 1,311 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.9 | +22.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.0 | +7.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.7 | +4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +4.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +2.4 | +2.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.2 | +3.2 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.2 | +2.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -5.6 | -14.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.5 | -11.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.1 | -10.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.9 | -8.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.9 | -10.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.5 | -8.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.5 | -7.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.4 | -5.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.0 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | patched 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.32 — chr9:95,442,980-95,517,057 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BCNS, SLC65B1; previously NBCCS, PTCH |
| Gene groups (HGNC) | Solute carrier family 65 |
| Hallmark sets | HEDGEHOG_SIGNALING, WNT_BETA_CATENIN_SIGNALING, IL2_STAT5_SIGNALING |
| Reactome | 9 pathways, smallest: Ligand-receptor interactions; GLI proteins bind promoters of Hh responsive genes to promote transcription; Activation of SMO |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13635](https://www.uniprot.org/uniprotkb/Q13635) (Protein patched homolog 1):

> Negative regulator of the smoothened signaling pathway, which acts as a receptor for hedgehog (SHH, IHH and DHH) morphogens. In absence of hedgehog, acts as an inhibitor of smoothened protein (SMO) by preventing SMO access to cholesterol: mechanistically, acts as a cholesterol transporter, which depeletes cholesterol from the outer leaflet of plasma membrane, thereby preventing cholesterol-binding to the extracellular CRD region of SMO. Hedgehog-binding inhibits PTCH1 cholesterol transporter …

**Summary**, from NCBI Gene [5727](https://www.ncbi.nlm.nih.gov/gene/5727):

> This gene encodes a member of the patched family of proteins and a component of the hedgehog signaling pathway. Hedgehog signaling is important in embryonic development and tumorigenesis. The encoded protein is the receptor for the secreted hedgehog ligands, which include sonic hedgehog, indian hedgehog and desert hedgehog. Following binding by one of the hedgehog ligands, the encoded protein is trafficked away from the primary cilium, relieving inhibition of the G-protein-coupled receptor …

**Accessions** — [HGNC:9585](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9585) · Entrez [5727](https://www.ncbi.nlm.nih.gov/gene/5727) · UniProt [Q13635](https://www.uniprot.org/uniprotkb/Q13635) · Ensembl [ENSG00000185920](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185920)

## Data

Gene col 11753: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11753); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11753, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11753]; `tensor/DDL_lfc|DDL_z.npy` [11753]; `embed/gene_vectors.npy` [11753]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11753 or target_col == 11753). Every well: [[PTCH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTCH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
