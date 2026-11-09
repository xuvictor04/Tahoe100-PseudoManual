---
symbol: "N4BP2L1"
type: "gene"
col: 6318
ensembl_id: "ENSG00000139597"
name: "NEDD4 binding protein 2 like 1"
location: "13q13.1"
module: 23
arm: "+"
pooled_cpm: 11.0
n_lines_expressing: 49
n_dd_up: 41
n_dd_down: 18
n_dd_up_clean: 32
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# N4BP2L1

*NEDD4 binding protein 2 like 1* — 13q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.50× (z +26.1, q 0e+00, up in 40 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.444× (z -10.0, q 1e-20, down in 32 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Abemaciclib (drug)]] 0.5 µM: 0.598× (z -4.5, q 5e-04, down in 16 of 47 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AK9]] (+0.80, fdr 7e-06), [[PPP1R12A-AS2]] (+0.80, fdr 1e-05), [[THAP2]] (+0.78, fdr 1e-05); moves opposite to [[GNA12]] (-0.68, fdr 7e-05), [[TBC1D24]] (-0.68, fdr 3e-05), [[RNGTT]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6318.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.50×** | +26.1 | 0e+00 | 40/44 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.86×** | +15.9 | 0e+00 | 35/43 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.45×** | +15.6 | 0e+00 | 41/42 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.71×** | +11.8 | 6e-30 | 36/41 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.97×** | +11.8 | 7e-30 | 34/47 (A498, J82, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.30×** | +9.9 | 6e-21 | 28/41 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.22×** | +9.4 | 3e-19 | 29/45 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +7.8 | 4e-13 | 24/47 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **3.64×** | +7.8 | 4e-13 | 32/45 (HEC-1-A, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.88×** | +7.7 | 5e-13 | 30/45 (C32, HEC-1-A, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.80×** | +7.2 | 2e-11 | 28/46 (A498, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +6.0 | 1e-07 | 16/37 (hTERT-HPNE, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.55×** | +5.2 | 9e-06 | 24/45 (J82, A-427, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.48×** | +4.7 | 1e-04 | 13/45 (HS-578T, NCI-H460, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **2.15×** | +4.6 | 1e-04 | 13/45 (HEC-1-A, A498, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +4.3 | 6e-04 | 15/45 (C32, HT-29, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.56×** | +3.9 | 0.003 | 8/42 (HEC-1-A, CFPAC-1, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.36×** | +3.8 | 0.004 | 11/44 (KATO III, HT-29, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.004 | 11/46 (SW480, C32, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6318.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.444×** | -10.0 | 1e-20 | 32/46 (SW1417, COLO 205, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.523×** | -8.0 | 5e-13 | 29/46 (Panc 03.27, SNU-423, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.558×** | -7.1 | 2e-10 | 28/46 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **0.598×** | -6.3 | 4e-08 | 27/46 (Panc 03.27, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.366×** | -6.1 | 1e-07 | 19/46 (SW480, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.625×** | -5.8 | 8e-07 | 19/44 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.661×** | -5.1 | 3e-05 | 20/46 (SW480, COLO 205, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.598×** | -4.5 | 5e-04 | 16/47 (SW480, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.485×** | -4.4 | 8e-04 | 12/44 (MIA PaCa-2, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.504×** | -4.1 | 0.002 | 12/42 (HepG2/C3A, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.508×** | -4.1 | 0.002 | 14/43 (HepG2/C3A, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.516×** | -4.0 | 0.003 | 15/38 (COLO 205, A498, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.543×** | -3.7 | 0.010 | 11/46 (A498, HT-29, …) | two highest doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.746×** | -3.6 | 0.013 | 15/46 (SW480, SNU-423, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.753×** | -3.5 | 0.020 | 13/46 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.761×** | -3.3 | 0.027 | 20/45 (SW480, PANC-1, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.708×** | -3.0 | 0.082 | 9/45 (CFPAC-1, RKO, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.73 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6318. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 11.7 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.98× (z +16.1) | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 45.8 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +13.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.170× (z -10.8) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.0587× (z -8.5) |
| [[J82 (line)]] | alt | 15.3 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +21.2) | [[Dinaciclib (drug)]] 5 µM 0.111× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 23.8 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.0754× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 14.2 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +9.4) | [[Belinostat (drug)]] 5 µM 0.177× (z -11.5) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.278× (z -8.5) |
| [[A498 (line)]] | wt | 13.4 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 6.00× (z +11.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.240× (z -9.2) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 19.6 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0512× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[TAK-733 (drug)]] 5 µM 0.0465× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 20.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.11× (z +14.4) | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -11.4) ⚠ cell-cycle shift, explains ~87% of this change |
| [[PANC-1 (line)]] | alt | 7.37 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +20.7) | — |
| [[HCT15 (line)]] | alt | 25.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.71× (z +12.7) | — |
| [[HepG2_C3A (line)]] | wt | 65.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +10.6) | [[Lonafarnib (drug)]] 5 µM 0.0642× (z -9.6) ⚠ toxic |
| [[HOP62 (line)]] | alt | 5.99 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.95× (z +12.8) | — |
| [[LoVo (line)]] | wt | 8.96 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +17.2) | — |
| [[NCI-H1792 (line)]] | alt | 12.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.06× (z +13.4) | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 8.43 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.75× (z +16.2) | — |
| [[NCI-H460 (line)]] | wt | 4.49 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +14.5) | — |
| [[SW 900 (line)]] | alt | 15.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +12.6) | [[Docetaxel (drug)]] 0.05 µM 0.0948× (z -11.2) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 5.51 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0713× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 8.30 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +11.0) | — |
| [[H4 (line)]] | wt | 9.44 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0640× (z -8.5) ⚠ cell-cycle shift, explains ~80% of this change |
| [[hTERT-HPNE (line)]] | wt | 13.7 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0854× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 6.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +11.7) | — |
| [[NCI-H1573 (line)]] | alt | 5.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.32× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 4.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 7.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.39× (z +12.2) | — |
| [[RKO (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.145× (z -8.8) ⚠ cell-cycle shift, explains ~87% of this change |
| [[RPMI-7951 (line)]] | alt | 15.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +10.0) | — |
| [[SHP-77 (line)]] | alt | 13.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 3.81 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0361× (z -10.8) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 11.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.81× (z +9.1) | — |
| [[A-427 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6318), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 8 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AK9]] | +0.80 | +0.83 / +0.62 | both halves | 7e-06 |  |
| [[PPP1R12A-AS2]] | +0.80 | +0.78 / +0.53 | both halves | 1e-05 |  |
| [[THAP2]] | +0.78 | +0.78 / +0.54 | both halves | 1e-05 |  |
| [[C3orf38]] | +0.78 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[ATE1OSP]] | +0.77 | +0.76 / +0.45 | both halves | 3e-05 |  |
| [[OXA1L-DT]] | +0.76 | +0.78 / +0.41 | both halves | 4e-05 |  |
| [[ABCA10]] | +0.75 | +0.82 / +0.49 | both halves | 1e-05 |  |
| [[MGAM]] | +0.75 | +0.77 / +0.50 | both halves | 1e-05 |  |
| [[TMEM202-AS1]] | +0.74 | +0.76 / +0.38 | both halves | 6e-05 |  |
| [[TAS2R4]] | +0.74 | +0.76 / +0.47 | both halves | 2e-05 |  |
| [[CDKL3]] | +0.74 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[CASS4]] | +0.74 | +0.70 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNA12]] | -0.68 | -0.71 / -0.38 | both halves | 7e-05 |  |
| [[TBC1D24]] | -0.68 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[RNGTT]] | -0.68 | -0.66 / -0.59 | both halves | 7e-06 |  |
| [[GTF2E2]] | -0.67 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[LRRC20]] | -0.67 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[SLX4]] | -0.66 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[STIMATE]] | -0.66 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[NOMO1]] | -0.66 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[DGKD]] | -0.66 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[AP3M2]] | -0.66 | -0.68 / -0.36 | both halves | 9e-05 |  |
| [[BLTP2]] | -0.65 | -0.66 / -0.58 | both halves | 8e-06 |  |
| [[TEX2]] | -0.65 | -0.45 / -0.59 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers N4BP2L1's level | compounds that target MTOR: 5 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 6.4% of all compounds | 0.041 | ⚠ off-target possible; 5 compounds |
| [[TOP2A]] | B | TOP2A activity lowers N4BP2L1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HECTD2]] | B | HECTD2 activity raises N4BP2L1's level | lines that do not express HECTD2 (5) vs lines expressing it (45) | 1.77× lower at baseline in the lines without HECTD2 | 0.071 | ⚠ within organs, on part of the lines; also absent: IMPG2, PHC1, TPST1; maybe low, not absent |
| [[LINC00504]] | B | LINC00504 activity raises N4BP2L1's level | lines that do not express LINC00504 (31) vs lines expressing it (19) | 1.37× lower at baseline in the lines without LINC00504 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC02930, ENSG00000287474 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.838). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (1.4, 16.4); signed map (23.7, -11.6). **Vector** length 116, 30.2% of its response variance represented; |z| ≥ 3 in 1,259 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.1 | +26.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.2 | +15.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +15.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +7.3 | +11.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.5 | +9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +7.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.6 | +7.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +7.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.7 | +4.6 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | -8.5 | -6.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | -8.4 | -7.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -7.7 | -8.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.6 | -5.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.5 | -10.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.8 | -2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.2 | -4.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.9 | -4.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.9 | -3.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.8 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | NEDD4 binding protein 2 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q13.1 — chr13:32,400,723-32,428,311 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CG018 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TBK1](https://www.uniprot.org/uniprotkb/Q5TBK1) (NEDD4-binding protein 2-like 1):

> Might play a role in adipocyte differentiation and triglyceride accumulation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25037](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25037) · Entrez [90634](https://www.ncbi.nlm.nih.gov/gene/90634) · UniProt [Q5TBK1](https://www.uniprot.org/uniprotkb/Q5TBK1) · Ensembl [ENSG00000139597](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139597)

## Data

Gene col 6318: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6318); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6318, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6318]; `tensor/DDL_lfc|DDL_z.npy` [6318]; `embed/gene_vectors.npy` [6318]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6318 or target_col == 6318). Every well: [[N4BP2L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/N4BP2L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
