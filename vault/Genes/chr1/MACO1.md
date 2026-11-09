---
symbol: "MACO1"
type: "gene"
col: 12826
ensembl_id: "ENSG00000204178"
name: "macoilin 1"
location: "1p36.11"
module: 3
arm: "+"
pooled_cpm: 91.51
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 21
n_dd_up_clean: 14
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# MACO1

*macoilin 1* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.95× (z +11.8, q 2e-29, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.435× (z -15.6, q 0e+00, down in 43 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.705× (z -9.2, q 6e-18, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MXD4]] (+0.73, fdr 7e-06), [[RAB6A]] (+0.72, fdr 7e-06), [[KLHL7]] (+0.71, fdr 7e-06); moves opposite to [[POGLUT1]] (-0.68, fdr 7e-06), [[SRCAP]] (-0.67, fdr 1e-05), [[TRIM44]] (-0.67, fdr 8e-06).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DAB2]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Pimozide (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12826.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.95×** | +11.8 | 2e-29 | 44/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.71×** | +10.0 | 3e-21 | 44/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.58×** | +8.6 | 2e-15 | 44/48 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +8.4 | 8e-15 | 36/48 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +7.6 | 4e-12 | 32/49 (RKO, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +6.9 | 4e-10 | 31/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +6.4 | 1e-08 | 29/48 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.56×** | +6.0 | 2e-07 | 38/49 (PANC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.8 | 8e-05 | 27/45 (SW480, A-427, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.20× | +4.8 | 9e-05 | 21/49 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.30×** | +4.7 | 1e-04 | 31/47 (NCI-H2030, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.004 | 21/48 (PANC-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.23×** | +3.8 | 0.005 | 21/48 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.031 | 17/48 (CFPAC-1, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 1.13× | +3.3 | 0.034 | 11/48 (LS 180, HT-29, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.037 | 21/47 (NCI-H2030, LS 180, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12826.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.435×** | -15.6 | 0e+00 | 43/48 (COLO 205, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.422×** | -15.5 | 0e+00 | 40/43 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.481×** | -13.7 | 4e-40 | 48/48 (AsPC-1, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.577×** | -9.5 | 4e-19 | 33/45 (A-172, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.705×** | -9.2 | 6e-18 | 28/48 (AsPC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.646×** | -8.2 | 3e-14 | 37/48 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.660×** | -7.4 | 8e-12 | 34/48 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.497×** | -6.8 | 6e-10 | 39/48 (Hs 766T, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.788×** | -6.3 | 2e-08 | 31/48 (HS-578T, AsPC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.531×** | -6.2 | 3e-08 | 35/48 (AsPC-1, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.549×** | -5.9 | 2e-07 | 39/48 (AsPC-1, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.756×** | -5.2 | 9e-06 | 30/48 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.599×** | -5.0 | 3e-05 | 32/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.618×** | -4.7 | 1e-04 | 26/48 (AsPC-1, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.843× | -4.5 | 3e-04 | 22/48 (AsPC-1, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **0.782×** | -4.4 | 4e-04 | 29/48 (HS-578T, hTERT-HPNE, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.816×** | -3.8 | 0.004 | 22/48 (CFPAC-1, HOP62, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.839× | -3.3 | 0.025 | 18/48 (CFPAC-1, A549, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.845× | -3.1 | 0.037 | 18/49 (LS 180, SNU-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.848× | -3.1 | 0.042 | 22/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12826. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 158 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -22.8) |
| [[A-172 (line)]] | wt | 75.7 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -19.8) |
| [[CFPAC-1 (line)]] | alt | 152 | 2 | 6 (5 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.04× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.137× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.472× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 65.9 | 2 | 6 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.33× (z +9.2) | [[Homoharringtonine (drug)]] 0.05 µM 0.328× (z -12.8) |
| [[Hs 766T (line)]] | wt | 129 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.239× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.386× (z -10.2) |
| [[HS-578T (line)]] | alt | 187 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.216× (z -18.7) |
| [[NCI-H2347 (line)]] | alt | 107 | 0 | 7 (6 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.286× (z -14.7) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.378× (z -11.4) |
| [[PANC-1 (line)]] | alt | 60.4 | 6 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.78× (z +12.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.288× (z -14.8) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 84.6 | 4 (1 ⚠) | 3 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.32× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.299× (z -15.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 44.8 | 6 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.66× (z +9.2) | — |
| [[KATO III (line)]] | alt | 79.0 | 2 | 4 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.25× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.267× (z -13.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 145 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.397× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 107 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.258× (z -12.1) |
| [[J82 (line)]] | alt | 100 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -13.7) |
| [[LS 180 (line)]] | wt | 95.5 | 3 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.72× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 40.5 | 5 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.50× (z +11.6) | — |
| [[RPMI-7951 (line)]] | alt | 132 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.484× (z -10.6) |
| [[SW 900 (line)]] | alt | 118 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -13.2) |
| [[AN3 CA (line)]] | alt | 173 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -18.6) |
| [[HT-29 (line)]] | alt | 67.7 | 1 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.47× (z +9.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.269× (z -13.2) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 119 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.321× (z -11.4) |
| [[SW1417 (line)]] | alt | 73.6 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +9.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.304× (z -13.0) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 96.5 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.331× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.455× (z -8.7) |
| [[H4 (line)]] | wt | 129 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 127 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 28.7 | 3 | 0 | [[Belinostat (drug)]] 5 µM 4.58× (z +11.3) | — |
| [[SNU-423 (line)]] | alt | 71.9 | 1 | 2 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.30× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.566× (z -9.9) |
| [[C32 (line)]] | wt | 95.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -11.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 88.1 | 1 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.27× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.0825× (z -19.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 91.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 61.2 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.330× (z -11.5) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 88.0 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.40× (z +9.8) | — |
| [[RKO (line)]] | wt | 76.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +10.6) | — |
| [[SW48 (line)]] | wt | 82.6 | 1 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.76× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.190× (z -12.1) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 64.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.389× (z -8.8) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 161 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.56× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 52.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.260× (z -11.1) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 83.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 55.2 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.37× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -20.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -15.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 80.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 108 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12826), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MXD4]] | +0.73 | +0.62 / +0.82 | both halves | 7e-06 |  |
| [[RAB6A]] | +0.72 | +0.80 / +0.62 | both halves | 7e-06 |  |
| [[KLHL7]] | +0.71 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[CARD19]] | +0.71 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[ULK1]] | +0.70 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[SPSB3]] | +0.70 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[MGST3]] | +0.69 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[CAMLG]] | +0.69 | +0.68 / +0.57 | both halves | 9e-06 |  |
| [[BAHD1]] | +0.68 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[MOSPD3]] | +0.68 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[MRPL55]] | +0.68 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[WIPI2]] | +0.68 | +0.66 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGLUT1]] | -0.68 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[SRCAP]] | -0.67 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[TRIM44]] | -0.67 | -0.64 / -0.58 | both halves | 8e-06 |  |
| [[ZC3H7B]] | -0.66 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[SF3B3]] | -0.66 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[ST7L]] | -0.66 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[UTP20]] | -0.66 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[ZNF507]] | -0.65 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[PRRC2A]] | -0.65 | -0.48 / -0.71 | both halves | 2e-05 |  |
| [[GUF1]] | -0.64 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[NCR3LG1]] | -0.64 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[NHLRC2]] | -0.64 | -0.62 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DAB2]] | B | DAB2 activity raises MACO1's level | lines that do not express DAB2 (18) vs lines expressing it (32) | 1.32× lower at baseline in the lines without DAB2 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: C9, NNMT, DPYSL3 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Pimozide (drug)]] 0.05 µM | C | MACO1's natural level raises the cells' numbers under Pimozide 0.05 µM (protects the cells) | MACO1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.69 | 0.285 over the table, 0.058 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | MACO1's natural level raises the cells' numbers under ERK5-IN-2 0.5 µM (protects the cells) | MACO1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63 | 0.403 over the table, 0.040 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.729). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (3.2, -16.2); signed map (-23.8, 11.5). **Vector** length 152, 52.6% of its response variance represented; |z| ≥ 3 in 1,380 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +9.4 | +11.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +9.4 | +10.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.6 | +8.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.4 | +8.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +7.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.4 | +6.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.5 | +4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.8 | +2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.3 | +3.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.7 | -13.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -9.4 | -9.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.5 | -7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.0 | -8.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -6.5 | -3.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.3 | -5.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.8 | -6.8 |
|  | [[EX229 (drug)]] 5 µM |  | -5.3 | -4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.8 | -4.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.7 | -6.2 |

## What is on record

|  |  |
|---|---|
| Name | macoilin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:25,430,858-25,500,209 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10747; previously TMEM57 |
| Reactome | 5 pathways, smallest: RHOC GTPase cycle; RHOA GTPase cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5G2](https://www.uniprot.org/uniprotkb/Q8N5G2) (Macoilin):

> Plays a role in the regulation of neuronal activity.

**Summary**, from NCBI Gene [55219](https://www.ncbi.nlm.nih.gov/gene/55219):

> Predicted to enable microtubule binding activity. Involved in neuronal signal transduction. Located in rough endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25572](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25572) · Entrez [55219](https://www.ncbi.nlm.nih.gov/gene/55219) · UniProt [Q8N5G2](https://www.uniprot.org/uniprotkb/Q8N5G2) · Ensembl [ENSG00000204178](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204178)

## Data

Gene col 12826: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12826); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12826, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12826]; `tensor/DDL_lfc|DDL_z.npy` [12826]; `embed/gene_vectors.npy` [12826]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12826 or target_col == 12826). Every well: [[MACO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MACO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
