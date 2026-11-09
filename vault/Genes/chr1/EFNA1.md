---
symbol: "EFNA1"
type: "gene"
col: 9782
ensembl_id: "ENSG00000169242"
name: "ephrin A1"
location: "1q22"
module: 14
arm: "+"
pooled_cpm: 36.68
n_lines_expressing: 37
n_dd_up: 23
n_dd_down: 28
n_dd_up_clean: 18
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 29
direction_downstream: 28
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# EFNA1

*ephrin A1* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.69× (z +8.1, q 2e-13, up in 16 of 34 measured lines) ⚠ cell-cycle shift, explains ~59% of this change. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 2.01× (z +7.3, q 5e-11, up in 27 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.248× (z -15.2, q 0e+00, down in 33 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP3K8]] (+0.76, fdr 7e-06), [[TNFAIP2]] (+0.74, fdr 7e-06), [[REL]] (+0.73, fdr 7e-06); moves opposite to [[MPP3]] (-0.62, fdr 7e-06), [[SHLD2]] (-0.61, fdr 1e-05), [[NBPF15]] (-0.59, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 29 arrows point to it, the strongest [[ELF3]] → it (grade B ⚠); 28 go from it, the strongest it → [[ELF3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9782.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.69×** | +8.1 | 2e-13 | 16/34 (SNU-423, PANC-1, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.15×** | +8.0 | 3e-13 | 20/34 (PANC-1, NCI-H1573, …) | rises with dose | composition shift; position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **2.01×** | +7.3 | 5e-11 | 27/33 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.50×** | +6.6 | 5e-09 | 24/36 (NCI-H1573, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +6.3 | 3e-08 | 20/32 (SNU-423, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.65×** | +6.0 | 1e-07 | 27/36 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.62×** | +5.8 | 4e-07 | 23/35 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.69×** | +5.8 | 6e-07 | 23/35 (NCI-H460, NCI-H23, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.64×** | +5.2 | 1e-05 | 22/34 (NCI-H23, MIA PaCa-2, …) | two highest doses |  |
| [[Trametinib (drug)]] 5 µM |  | **1.45×** | +5.2 | 1e-05 | 21/36 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.55×** | +4.9 | 4e-05 | 18/33 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.55×** | +4.9 | 6e-05 | 19/35 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.50×** | +4.4 | 5e-04 | 17/33 (AsPC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.50×** | +4.1 | 0.002 | 19/32 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.47×** | +4.0 | 0.003 | 18/34 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.012 | 18/34 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.012 | 15/33 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.25×** | +3.4 | 0.019 | 15/36 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.036 | 12/35 (AsPC-1, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9782.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.248×** | -15.2 | 0e+00 | 33/35 (HepG2/C3A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.294×** | -13.3 | 4e-38 | 32/35 (LS 180, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.296×** | -12.8 | 4e-35 | 25/28 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.413×** | -9.7 | 6e-20 | 29/34 (AsPC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.430×** | -9.2 | 3e-18 | 31/34 (LoVo, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.442×** | -8.9 | 5e-17 | 24/33 (LS 180, COLO 205, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.487×** | -7.8 | 3e-13 | 26/34 (LoVo, HepG2/C3A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.600×** | -5.6 | 2e-06 | 20/34 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.722×** | -5.0 | 3e-05 | 22/36 (C32, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.640×** | -4.6 | 2e-04 | 22/34 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.433×** | -4.4 | 5e-04 | 23/33 (LoVo, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.678×** | -4.2 | 0.001 | 18/34 (CFPAC-1, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.681×** | -4.2 | 0.001 | 21/35 (A549, LoVo, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.687×** | -4.1 | 0.002 | 19/34 (NCI-H460, NCI-H2030, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.688×** | -4.1 | 0.002 | 20/35 (HepG2/C3A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[EX229 (drug)]] 5 µM |  | **0.464×** | -4.1 | 0.002 | 21/32 (SW1417, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.469×** | -4.0 | 0.002 | 22/34 (LoVo, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.692×** | -3.9 | 0.003 | 17/34 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.704×** | -3.8 | 0.004 | 17/34 (SK-MEL-2, C32, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.712×** | -3.7 | 0.005 | 16/33 (Panc 03.27, NCI-H2347, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.798×** | -3.5 | 0.012 | 13/36 (A549, NCI-H1573, …) | rises with dose | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.522×** | -3.4 | 0.014 | 17/33 (LoVo, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.64 per unit of S-phase module lfc, +0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9782. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 51.0 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -15.3) |
| [[LoVo (line)]] | wt | 74.4 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0885× (z -20.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.117× (z -17.8) |
| [[NCI-H1573 (line)]] | alt | 36.6 | 5 (4 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 6.61× (z +11.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 20.9× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.161× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 66.6 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0667× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.230× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 59.0 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0921× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.220× (z -9.9) |
| [[A549 (line)]] | wt | 70.4 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0409× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0544× (z -17.4) |
| [[HepG2_C3A (line)]] | wt | 149 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0247× (z -21.4) |
| [[AsPC-1 (line)]] | alt | 45.2 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -11.4) |
| [[KATO III (line)]] | alt | 48.3 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0587× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0969× (z -16.9) |
| [[LS 180 (line)]] | wt | 59.7 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0857× (z -20.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.112× (z -18.2) |
| [[PANC-1 (line)]] | alt | 20.7 | 4 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +15.3) ⚠ cell-cycle shift, explains ~59% of this change | [[Dinaciclib (drug)]] 5 µM 0.186× (z -9.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 68.8 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -13.1) |
| [[SW480 (line)]] | alt | 24.1 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.179× (z -13.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.205× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 46.8 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -11.1) |
| [[HT-29 (line)]] | alt | 55.3 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0772× (z -19.3) |
| [[MIA PaCa-2 (line)]] | alt | 28.5 | 3 (3 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 2.72× (z +19.7) ⚠ position not correctable | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.206× (z -9.0) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 37.5 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.202× (z -8.5) |
| [[A-172 (line)]] | wt | 20.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.97× (z +13.3) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 6.89× (z +8.7) | — |
| [[BT-474 (line)]] | alt | 94.1 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +12.4) ⚠ cell-cycle shift, explains ~59% of this change | [[Dinaciclib (drug)]] 5 µM 0.0700× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.127× (z -10.9) |
| [[COLO 205 (line)]] | alt | 60.1 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.105× (z -14.8) |
| [[C32 (line)]] | wt | 33.1 | 0 | 2 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.309× (z -9.1) |
| [[HCT15 (line)]] | alt | 41.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -10.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 25.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 78.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.95× (z +11.2) ⚠ position not correctable | [[Bortezomib (drug)]] 0.05 µM 0.138× (z -9.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[Panc 03.27 (line)]] | alt | 51.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +10.9) ⚠ cell-cycle shift, explains ~59% of this change | [[Dinaciclib (drug)]] 5 µM 0.230× (z -9.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 29.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +15.7) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[CHP-212 (line)]] | wt | 10.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +8.8) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[J82 (line)]] | alt | 22.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.47× (z +11.6) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[NCI-H23 (line)]] | alt | 44.0 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.84× (z +9.8) ⚠ position not correctable | — |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.152× (z -9.9) |
| [[A-427 (line)]] | wt | 6.22 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.62 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.27 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.69 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.84 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.15 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.65 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 85.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.94 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.58 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.22 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.55 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.96 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9782), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP3K8]] | +0.76 | +0.72 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[TNFAIP2]] | +0.74 | +0.68 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[REL]] | +0.73 | +0.65 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ELF3]] | +0.71 | +0.61 / +0.77 | both halves | 7e-06 |  |
| [[BCL3]] | +0.70 | +0.62 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[GBP2]] | +0.67 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[IRF1]] | +0.67 | +0.60 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[RAB9A]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[STAP2]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[B2M]] | +0.65 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[STAT5A]] | +0.65 | +0.53 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[DDR1]] | +0.65 | +0.67 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPP3]] | -0.62 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[SHLD2]] | -0.61 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[NBPF15]] | -0.59 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[SEC14L1]] | -0.58 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[ITGB1BP1]] | -0.58 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[NBPF20]] | -0.57 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[DCTD]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[THOC5]] | -0.56 | -0.38 / -0.63 | both halves | 6e-05 |  |
| [[LYPLA1]] | -0.55 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[CROCCP3-1]] | -0.55 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[TPD52L2]] | -0.55 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[TTL]] | -0.54 | -0.47 / -0.56 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 25, C 4. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF3]] | B | ELF3 activity raises EFNA1's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 3.06× lower at baseline in the lines without ELF3 | 0.001 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[FRK]] | B | FRK activity raises EFNA1's level | lines that do not express FRK (22) vs lines expressing it (28) | 3.00× lower at baseline in the lines without FRK | 0.002 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |
| [[FRMD4B]] | B | FRMD4B activity raises EFNA1's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 2.83× lower at baseline in the lines without FRMD4B | 0.003 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[RBM47]] | B | RBM47 activity raises EFNA1's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 2.88× lower at baseline in the lines without RBM47 | 0.005 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[HNF1B]] | B | HNF1B activity raises EFNA1's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 2.85× lower at baseline in the lines without HNF1B | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |
| [[PDZK1IP1]] | B | PDZK1IP1 activity raises EFNA1's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 2.72× lower at baseline in the lines without PDZK1IP1 | 0.009 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[RASSF6]] | B | RASSF6 activity raises EFNA1's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 2.85× lower at baseline in the lines without RASSF6 | 0.009 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[SHROOM3]] | B | SHROOM3 activity raises EFNA1's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 1.95× lower at baseline in the lines without SHROOM3 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[FAAH2]] | B | FAAH2 activity raises EFNA1's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 2.64× lower at baseline in the lines without FAAH2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[TRIM31]] | B | TRIM31 activity raises EFNA1's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 3.10× lower at baseline in the lines without TRIM31 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[MUC16]] | B | MUC16 activity raises EFNA1's level | lines that do not express MUC16 (38) vs lines expressing it (12) | 2.82× lower at baseline in the lines without MUC16 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSDMC, S100A9, STEAP4 |
| [[MUC1]] | B | MUC1 activity raises EFNA1's level | lines that do not express MUC1 (25) vs lines expressing it (25) | 2.36× lower at baseline in the lines without MUC1 | 0.038 | ⚠ within organs, on part of the lines; also absent: TACSTD2, UCA1, RNF223 |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 25, C 3. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF3]] | B | EFNA1 activity raises ELF3's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 4.61× lower at baseline in the lines without EFNA1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[FRK]] | B | EFNA1 activity raises FRK's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 3.60× lower at baseline in the lines without EFNA1 | 0.008 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[DDR1]] | B | EFNA1 activity raises DDR1's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 2.77× lower at baseline in the lines without EFNA1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[FAAH2]] | B | EFNA1 activity raises FAAH2's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 4.31× lower at baseline in the lines without EFNA1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[FRMD4B]] | B | EFNA1 activity raises FRMD4B's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 3.05× lower at baseline in the lines without EFNA1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[ATP1B1]] | B | EFNA1 activity raises ATP1B1's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 2.69× lower at baseline in the lines without EFNA1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[RHOU]] | B | EFNA1 activity raises RHOU's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 2.24× lower at baseline in the lines without EFNA1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[MTUS1]] | B | EFNA1 activity raises MTUS1's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 3.41× lower at baseline in the lines without EFNA1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[TSPAN15]] | B | EFNA1 activity raises TSPAN15's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 2.46× lower at baseline in the lines without EFNA1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[SLC37A1]] | B | EFNA1 activity raises SLC37A1's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 2.18× lower at baseline in the lines without EFNA1 | 0.035 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[RASGEF1B]] | B | EFNA1 activity raises RASGEF1B's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 2.10× lower at baseline in the lines without EFNA1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[SLC50A1]] | B | EFNA1 activity raises SLC50A1's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 1.35× lower at baseline in the lines without EFNA1 | 0.042 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.690). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.3, 4.0); signed map (45.3, 6.8). **Vector** length 129, 38.4% of its response variance represented; |z| ≥ 3 in 1,159 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trametinib (drug)]] 0.5 µM |  | +6.5 | +5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +6.4 | +8.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.3 | +7.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +6.0 | +6.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +5.4 | +5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +5.2 | +5.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.5 | -9.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.8 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -9.2 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -3.8 | -2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.8 | -4.0 |
|  | [[EX229 (drug)]] 5 µM |  | -3.7 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | ephrin A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:155,127,876-155,134,899 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LERK1, ECKLG, GMAN; previously TNFAIP4, EPLG1 |
| Gene groups (HGNC) | Ephrins |
| Hallmark sets | HYPOXIA, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 5 pathways, smallest: EPHA-mediated growth cone collapse; EPH-ephrin mediated repulsion of cells; EPH-Ephrin signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P20827](https://www.uniprot.org/uniprotkb/P20827) (Ephrin-A1):

> Cell surface GPI-bound ligand for Eph receptors, a family of receptor tyrosine kinases which are crucial for migration, repulsion and adhesion during neuronal, vascular and epithelial development. Binds promiscuously Eph receptors residing on adjacent cells, leading to contact-dependent bidirectional signaling into neighboring cells. Involved in angiogenesis, regulating vascular endothelial cell differentiation and migration through activation of EPHA2. Acts as a ligand for EPHA3, inhibiting …

**Summary**, from NCBI Gene [1942](https://www.ncbi.nlm.nih.gov/gene/1942):

> This gene encodes a member of the ephrin (EPH) family. The ephrins and EPH-related receptors comprise the largest subfamily of receptor protein-tyrosine kinases and have been implicated in mediating developmental events, especially in the nervous system and in erythropoiesis. Based on their structures and sequence relationships, ephrins are divided into the ephrin-A (EFNA) class, which are anchored to the membrane by a glycosylphosphatidylinositol linkage, and the ephrin-B (EFNB) class, which …

**Accessions** — [HGNC:3221](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3221) · Entrez [1942](https://www.ncbi.nlm.nih.gov/gene/1942) · UniProt [P20827](https://www.uniprot.org/uniprotkb/P20827) · Ensembl [ENSG00000169242](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169242)

## Data

Gene col 9782: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9782); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9782, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9782]; `tensor/DDL_lfc|DDL_z.npy` [9782]; `embed/gene_vectors.npy` [9782]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9782 or target_col == 9782). Every well: [[EFNA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFNA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
