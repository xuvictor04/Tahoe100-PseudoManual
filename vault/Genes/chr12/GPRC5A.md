---
symbol: "GPRC5A"
type: "gene"
col: 280
ensembl_id: "ENSG00000013588"
name: "G protein-coupled receptor class C group 5 member A"
location: "12p13.1"
module: 31
arm: "+"
pooled_cpm: 542.12
n_lines_expressing: 38
n_dd_up: 4
n_dd_down: 47
n_dd_up_clean: 2
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 41
direction_downstream: 56
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# GPRC5A

*G protein-coupled receptor class C group 5 member A* — 12p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.36× (z +5.2, q 1e-04, up in 21 of 37 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.23× (z +5.0, q 2e-04, up in 16 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 3 lines (PANC-1 6.14×, NCI-H23 8.61×, MIA PaCa-2 3.82×); [[Trametinib (drug)]] 5 µM in 1 line (NCI-H23 2.94×; ⚠ cell-cycle shift, would explain all of this change); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (C32 3.04×; ⚠ cell-cycle shift, explains ~69% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (NCI-H23 2.64×); [[Trametinib (drug)]] 0.5 µM in 1 line (NCI-H23 2.47×).
> Pooled over the cell lines (median), lowered significantly by 47 drug-doses (21 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.308× (z -28.1, q 0e+00, down in 34 of 36 measured lines) ⚠ position correction uncertain. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.402× (z -21.7, q 0e+00, down in 35 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OXSR1]] (+0.66, fdr 7e-06), [[JUP]] (+0.65, fdr 7e-06), [[GDPGP1]] (+0.64, fdr 1e-05); moves opposite to [[RCBTB2]] (-0.56, fdr 1e-04), [[NNT]] (-0.55, fdr 4e-05), [[EXOSC10]] (-0.51, fdr 9e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 41 arrows point to it, the strongest [[LIPH]] → it (grade B ⚠); 56 go from it, the strongest it → [[CLMN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 280.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 3 lines (PANC-1 6.14×, NCI-H23 8.61×, MIA PaCa-2 3.82×); [[Trametinib (drug)]] 5 µM in 1 line (NCI-H23 2.94×; ⚠ cell-cycle shift, would explain all of this change); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (C32 3.04×; ⚠ cell-cycle shift, explains ~69% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (NCI-H23 2.64×); [[Trametinib (drug)]] 0.5 µM in 1 line (NCI-H23 2.47×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.36×** | +5.2 | 1e-04 | 21/37 (LS 180, A-172, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +5.0 | 2e-04 | 16/36 (A-172, HCT15, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.66×** | +4.5 | 0.001 | 22/36 (SW480, C32, …) | top dose only | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | 1.15× | +3.5 | 0.072 | 13/37 (NCI-H1792, SW 900, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.22×** | +3.4 | 0.072 | 15/37 (PANC-1, KATO III, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 1.43× | +3.2 | 0.14 | 19/37 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +3.1 | 0.16 | 13/37 (CHP-212, HCT15, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 57 in all, 24 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 47 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 280.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | **0.308×** | -28.1 | 0e+00 | 34/36 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.402×** | -21.7 | 0e+00 | 35/37 (MIA PaCa-2, SW1417, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ position correction uncertain | **0.299×** | -20.4 | 0e+00 | 33/36 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.390×** | -15.3 | 0e+00 | 32/36 (Hs 766T, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.408×** | -14.6 | 0e+00 | 30/33 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.446×** | -13.6 | 2e-40 | 28/36 (KATO III, LS 180, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.521×** | -11.0 | 3e-26 | 32/36 (MIA PaCa-2, SW1417, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.531×** | -10.4 | 1e-23 | 30/37 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.541×** | -10.4 | 2e-23 | 26/36 (KATO III, LoVo, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.558×** | -9.5 | 2e-19 | 31/36 (MIA PaCa-2, SW48, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.562×** | -9.3 | 5e-19 | 30/35 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.566×** | -9.2 | 1e-18 | 28/35 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.419×** | -7.7 | 7e-13 | 32/36 (SW1417, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.658×** | -7.1 | 7e-11 | 27/36 (SW48, Panc 03.27, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.655×** | -6.9 | 3e-10 | 28/38 (MIA PaCa-2, SW48, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.666×** | -6.8 | 3e-10 | 27/36 (BT-474, LS 180, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.485×** | -6.4 | 5e-09 | 28/36 (MIA PaCa-2, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.504×** | -6.0 | 4e-08 | 28/36 (SW1417, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.513×** | -5.9 | 1e-07 | 24/36 (SW48, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.523×** | -5.7 | 3e-07 | 28/36 (MIA PaCa-2, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.794×** | -5.5 | 1e-06 | 21/36 (NCI-H1573, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.785×** | -4.1 | 9e-04 | 19/36 (KATO III, LS 180, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.849× | -3.9 | 0.002 | 15/36 (LoVo, C32, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.662×** | -3.6 | 0.005 | 18/35 (MIA PaCa-2, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **0.806×** | -3.6 | 0.005 | 16/36 (NCI-H2347, NCI-H1792, …) | all doses, flat | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.670×** | -3.5 | 0.007 | 17/37 (NCI-H2030, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.60 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 280. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 1,555 | 1 | 21 (14 ⚠) | [[TAK-901 (drug)]] 5 µM 3.82× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -38.5) |
| [[NCI-H2347 (line)]] | alt | 849 | 0 | 19 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -24.3) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -21.4) |
| [[SW1417 (line)]] | alt | 821 | 0 | 19 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -29.1) |
| [[BT-474 (line)]] | alt | 453 | 0 | 18 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -19.4) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -16.8) |
| [[KATO III (line)]] | alt | 1,064 | 0 | 18 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -36.6) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -19.7) |
| [[LoVo (line)]] | wt | 1,723 | 0 | 18 (11 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0886× (z -26.7) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -21.8) |
| [[SW48 (line)]] | wt | 1,408 | 0 | 17 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -27.8) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -27.7) |
| [[Panc 03.27 (line)]] | alt | 1,642 | 0 | 16 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -22.0) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -20.6) |
| [[LS 180 (line)]] | wt | 744 | 1 (1 ⚠) | 14 (11 ⚠) | [[Tucidinostat (drug)]] 0.5 µM 2.46× (z +9.2) ⚠ cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -24.7) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -21.9) |
| [[CFPAC-1 (line)]] | alt | 755 | 0 | 13 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -27.9) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -22.8) |
| [[NCI-H1573 (line)]] | alt | 1,445 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0785× (z -38.0) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 0.172× (z -17.9) |
| [[NCI-H1792 (line)]] | alt | 922 | 0 | 13 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -22.7) |
| [[A549 (line)]] | wt | 840 | 0 | 11 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -24.8) |
| [[HEC-1-A (line)]] | alt | 412 | 0 | 11 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -21.2) |
| [[AsPC-1 (line)]] | alt | 1,048 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -23.2) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -19.9) |
| [[Hs 766T (line)]] | wt | 754 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -30.7) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 0.143× (z -19.2) |
| [[HT-29 (line)]] | alt | 557 | 0 | 9 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.112× (z -19.6) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -16.3) |
| [[NCI-H2030 (line)]] | alt | 619 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -22.5) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -15.5) |
| [[NCI-H460 (line)]] | wt | 527 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -22.0) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -15.3) |
| [[PANC-1 (line)]] | alt | 400 | 1 | 7 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 6.14× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -22.1) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -16.7) |
| [[SW480 (line)]] | alt | 166 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -12.5) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 0.266× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 266 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -15.3) |
| [[C32 (line)]] | wt | 250 | 1 (1 ⚠) | 4 (2 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.04× (z +10.4) ⚠ cell-cycle shift, explains ~69% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -11.4) |
| [[HCT15 (line)]] | alt | 236 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -12.7) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -10.3) |
| [[HOP62 (line)]] | alt | 240 | 0 | 5 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.344× (z -9.7) ⚠ cell-cycle shift, explains ~55% of this change |
| [[CHP-212 (line)]] | wt | 195 | 1 | 3 (2 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 3.00× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -15.5) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 0.148× (z -10.3) |
| [[COLO 205 (line)]] | alt | 331 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -19.6) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 0.294× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 175 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.61× (z +11.0) | — |
| [[A498 (line)]] | wt | 275 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -12.2) |
| [[A-172 (line)]] | wt | 233 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 68.8 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 77.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 43.8 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 136 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.1 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 128 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 92.1 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 52.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 645 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 442 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.7 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 55.8 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 116 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 34.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 44.7 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 305 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 295 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 280), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OXSR1]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[JUP]] | +0.65 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[GDPGP1]] | +0.64 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[SEMA3B]] | +0.64 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[RHPN2]] | +0.64 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[FA2H]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[PIM1]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[GPRC5D-AS1]] | +0.61 | +0.53 / +0.65 | both halves | 1e-05 | ⚠ same locus (9.8 kb, same strand: neighbours can correlate without regulation) |
| [[RDH13]] | +0.60 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[CRYBG2]] | +0.60 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[UGCG]] | +0.59 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[SERPINB1]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[TMPRSS4]] | +0.58 | +0.59 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCBTB2]] | -0.56 | -0.62 / -0.34 | both halves | 1e-04 |  |
| [[NNT]] | -0.55 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[EXOSC10]] | -0.51 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[ZNF280D]] | -0.50 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[MCM3AP]] | -0.48 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[EFCAB2]] | -0.48 | -0.56 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*41 arrows, 41 of them with an alert ⚠; grade A 0, B 39, C 2. Shown: the 12 strongest; 29 more arrows (29 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LIPH]] | B | LIPH activity raises GPRC5A's level | lines that do not express LIPH (27) vs lines expressing it (23) | 4.66× lower at baseline in the lines without LIPH | 0.001 | ⚠ within organs, on part of the lines; also absent: CATSPERB, TC2N, SDR16C5 |
| [[FA2H]] | B | FA2H activity raises GPRC5A's level | lines that do not express FA2H (27) vs lines expressing it (23) | 4.08× lower at baseline in the lines without FA2H | 0.001 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises GPRC5A's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 4.13× lower at baseline in the lines without TMPRSS4 | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[JUP]] | B | JUP activity strengthens GPRC5A's drug response | lines that do not express JUP (9) vs lines expressing it (28) | the lines without JUP respond 0.54× as strongly (z diff +3.68); strongest at Panobinostat 5 µM: 0.88x vs 0.35x (z diff +5.7) | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671; target measured in part of the lines; artifact flags |
| [[GPRC5D-AS1]] | B | GPRC5D-AS1 activity raises GPRC5A's level | lines that do not express GPRC5D-AS1 (5) vs lines expressing it (45) | 6.47× lower at baseline in the lines without GPRC5D-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: S100A6, LGALS3BP, NMI; maybe low, not absent |
| [[CLMN]] | B | CLMN activity raises GPRC5A's level | lines that do not express CLMN (7) vs lines expressing it (43) | 5.40× lower at baseline in the lines without CLMN | 0.003 | ⚠ within organs, on part of the lines; also absent: ITPR3, NABP1, HTATIP2; maybe low, not absent |
| [[C1orf116]] | B | C1orf116 activity raises GPRC5A's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 3.99× lower at baseline in the lines without C1orf116 | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[KRT19]] | B | KRT19 activity raises GPRC5A's level | lines that do not express KRT19 (22) vs lines expressing it (28) | 4.06× lower at baseline in the lines without KRT19 | 0.004 | ⚠ within organs, on part of the lines; also absent: RNF223, TINAGL1, CLDN4 |
| [[CLDN4]] | B | CLDN4 activity raises GPRC5A's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 3.81× lower at baseline in the lines without CLDN4 | 0.006 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[LAMA3]] | B | LAMA3 activity raises GPRC5A's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 3.52× lower at baseline in the lines without LAMA3 | 0.006 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[SDR16C5]] | B | SDR16C5 activity raises GPRC5A's level | lines that do not express SDR16C5 (28) vs lines expressing it (22) | 4.34× lower at baseline in the lines without SDR16C5 | 0.007 | ⚠ within organs, on part of the lines; also absent: CATSPERB, FA2H, LIPH |
| [[PTK6]] | B | PTK6 activity raises GPRC5A's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 4.40× lower at baseline in the lines without PTK6 | 0.008 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent |

### Downstream of this gene

*56 arrows, 56 of them with an alert ⚠; grade A 0, B 56, C 0. Shown: the 12 strongest; 44 more arrows (44 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLMN]] | B | GPRC5A activity raises CLMN's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 3.34× lower at baseline in the lines without GPRC5A | 0.001 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[RHPN2]] | B | GPRC5A activity raises RHPN2's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 2.51× lower at baseline in the lines without GPRC5A | 0.002 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[UBE2H]] | B | GPRC5A activity raises UBE2H's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 1.81× lower at baseline in the lines without GPRC5A | 0.003 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[TNFAIP8]] | B | GPRC5A activity raises TNFAIP8's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 1.82× lower at baseline in the lines without GPRC5A | 0.003 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[KRT19]] | B | GPRC5A activity raises KRT19's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 5.14× lower at baseline in the lines without GPRC5A | 0.003 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[EZR]] | B | GPRC5A activity raises EZR's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 1.99× lower at baseline in the lines without GPRC5A | 0.004 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[GPRC5D-AS1]] | B | GPRC5A activity raises GPRC5D-AS1's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 3.00× lower at baseline in the lines without GPRC5A | 0.004 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[PERP]] | B | GPRC5A activity raises PERP's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 2.48× lower at baseline in the lines without GPRC5A | 0.005 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[MYO1E]] | B | GPRC5A activity raises MYO1E's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 2.52× lower at baseline in the lines without GPRC5A | 0.005 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[SEMA4B]] | B | GPRC5A activity raises SEMA4B's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 2.72× lower at baseline in the lines without GPRC5A | 0.005 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[OXSR1]] | B | GPRC5A activity raises OXSR1's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 1.55× lower at baseline in the lines without GPRC5A | 0.008 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[LAMA3]] | B | GPRC5A activity raises LAMA3's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 3.86× lower at baseline in the lines without GPRC5A | 0.012 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.637). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.2, 56.8); signed map (-1.6, 37.3). **Vector** length 131, 45.1% of its response variance represented; |z| ≥ 3 in 1,681 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +5.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.4 | -4.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.3 | -0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +6.0 | -13.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +5.2 | -10.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.2 | +4.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.3 | +2.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.0 | -11.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.7 | -7.7 |
|  | [[EX229 (drug)]] 5 µM |  | -5.3 | -6.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.2 | -15.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.2 | -6.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.9 | -6.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.7 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | G protein-coupled receptor class C group 5 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.1 — chr12:12,890,782-12,917,937 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RAIG1, TIG1, PEIG-1; previously RAI3 |
| Gene groups (HGNC) | G protein-coupled receptors, Class C orphans |
| Reactome | 3 pathways, smallest: HuR (ELAVL1) binds and stabilizes mRNA; Regulation of mRNA stability by proteins that bind AU-rich elements; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFJ5](https://www.uniprot.org/uniprotkb/Q8NFJ5) (Retinoic acid-induced protein 3):

> Orphan receptor. Could be involved in modulating differentiation and maintaining homeostasis of epithelial cells. This retinoic acid-inducible GPCR provide evidence for a possible interaction between retinoid and G protein signaling pathways. Functions as a negative modulator of EGFR signaling (By similarity). May act as a lung tumor suppressor.

**Summary**, from NCBI Gene [9052](https://www.ncbi.nlm.nih.gov/gene/9052):

> This gene encodes a member of the type 3 G protein-coupling receptor family, characterized by the signature 7-transmembrane domain motif. The encoded protein may be involved in interaction between retinoid acid and G protein signalling pathways. Retinoic acid plays a critical role in development, cellular growth, and differentiation. This gene may play a role in embryonic development and epithelial cell differentiation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9836](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9836) · Entrez [9052](https://www.ncbi.nlm.nih.gov/gene/9052) · UniProt [Q8NFJ5](https://www.uniprot.org/uniprotkb/Q8NFJ5) · Ensembl [ENSG00000013588](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000013588)

## Data

Gene col 280: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 280); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 280, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 280]; `tensor/DDL_lfc|DDL_z.npy` [280]; `embed/gene_vectors.npy` [280]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 280 or target_col == 280). Every well: [[GPRC5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPRC5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
