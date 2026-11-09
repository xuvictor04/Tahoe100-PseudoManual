---
symbol: "TBCK"
type: "gene"
col: 6978
ensembl_id: "ENSG00000145348"
name: "TBC1 domain containing kinase"
location: "4q24"
module: 28
arm: "+"
pooled_cpm: 116.92
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 29
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# TBCK

*TBC1 domain containing kinase* — 4q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.39× (z +4.3, q 0.008, up in 35 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (A-427 1.78×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 1.93×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (18 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.388× (z -12.9, q 2e-35, down in 48 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.448× (z -11.0, q 1e-25, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXOC4]] (+0.68, fdr 8e-06), [[METTL15]] (+0.66, fdr 1e-05), [[LINC01473]] (+0.64, fdr 7e-06); moves opposite to [[CEP295NL]] (-0.61, fdr 1e-05), [[SEMA3F]] (-0.59, fdr 2e-05), [[LYSMD4]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6978.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (A-427 1.78×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 1.93×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +4.3 | 0.008 | 35/47 (HEC-1-A, SK-MEL-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.23×** | +4.0 | 0.016 | 23/48 (A-427, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.34×** | +3.7 | 0.036 | 28/50 (NCI-H2347, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.66×** | +3.7 | 0.036 | 33/50 (HEC-1-A, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.2 | 0.14 | 21/48 (A-427, LoVo, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.14 | 16/48 (SW480, NCI-H2347, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.30× | +3.0 | 0.20 | 25/47 (C32, SW480, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6978.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.388×** | -12.9 | 2e-35 | 48/48 (COLO 205, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.402×** | -12.5 | 3e-33 | 47/48 (COLO 205, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.448×** | -11.0 | 1e-25 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.444×** | -10.7 | 2e-24 | 44/47 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.471×** | -10.3 | 1e-22 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.519×** | -9.0 | 3e-17 | 46/48 (HCT15, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.507×** | -8.6 | 8e-16 | 41/45 (SK-MEL-2, hTERT-HPNE, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.481×** | -8.3 | 8e-15 | 40/49 (COLO 205, HepG2/C3A, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.329×** | -8.0 | 1e-13 | 48/49 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.547×** | -7.9 | 1e-13 | 44/47 (HepG2/C3A, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.587×** | -7.0 | 1e-10 | 35/44 (KATO III, Panc 03.27, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.623×** | -6.5 | 5e-09 | 42/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.612×** | -6.4 | 5e-09 | 35/48 (A549, SNU-423, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **0.668×** | -5.5 | 2e-06 | 37/48 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.674×** | -5.4 | 3e-06 | 39/48 (KATO III, HCT15, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.477×** | -5.3 | 5e-06 | 35/48 (SNU-1, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.807×** | -4.1 | 0.001 | 32/49 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.749×** | -3.7 | 0.005 | 30/48 (KATO III, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.762×** | -3.6 | 0.008 | 30/48 (MIA PaCa-2, A549, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.789×** | -3.2 | 0.028 | 25/48 (CFPAC-1, SHP-77, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.778×** | -2.8 | 0.090 | 27/47 (MIA PaCa-2, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6978. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 102 | 0 | 13 (9 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.217× (z -18.4) |
| [[KATO III (line)]] | alt | 125 | 0 | 12 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -16.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.352× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 122 | 0 | 10 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.228× (z -16.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.264× (z -15.0) |
| [[COLO 205 (line)]] | alt | 186 | 0 | 9 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -22.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.265× (z -14.7) |
| [[HCT15 (line)]] | alt | 173 | 0 | 9 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.196× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.196× (z -13.1) |
| [[HepG2_C3A (line)]] | wt | 267 | 0 | 8 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.184× (z -15.5) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.411× (z -8.5) |
| [[LoVo (line)]] | wt | 145 | 0 | 8 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.321× (z -14.5) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.486× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 124 | 0 | 8 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.295× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 155 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.415× (z -8.5) |
| [[H4 (line)]] | wt | 176 | 0 | 7 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.212× (z -12.6) |
| [[LS 180 (line)]] | wt | 149 | 0 | 7 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -17.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.289× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 196 | 0 | 7 (6 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.151× (z -11.6) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.194× (z -10.0) |
| [[PANC-1 (line)]] | alt | 91.4 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.205× (z -19.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.277× (z -15.5) |
| [[hTERT-HPNE (line)]] | wt | 137 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.175× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[RPMI-7951 (line)]] | alt | 109 | 0 | 5 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.221× (z -12.8) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.325× (z -9.9) |
| [[SNU-1 (line)]] | wt | 118 | 0 | 5 (3 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0404× (z -13.9) |
| [[A549 (line)]] | wt | 99.3 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 136 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.326× (z -12.7) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.215× (z -9.4) |
| [[J82 (line)]] | alt | 53.4 | 0 | 4 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.302× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 134 | 0 | 4 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.118× (z -10.8) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 79.2 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.379× (z -9.1) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.410× (z -8.7) |
| [[A-427 (line)]] | wt | 119 | 1 (1 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.78× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[C32 (line)]] | wt | 147 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.284× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 146 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.327× (z -10.2) |
| [[CHP-212 (line)]] | wt | 200 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -11.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HOP62 (line)]] | alt | 119 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.260× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.366× (z -9.6) |
| [[HT-29 (line)]] | alt | 80.6 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.388× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.392× (z -9.4) |
| [[SW 900 (line)]] | alt | 130 | 0 | 3 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.156× (z -9.3) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 78.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.349× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HS-578T (line)]] | alt | 84.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[LOX-IMVI (line)]] | wt | 91.1 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.375× (z -9.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RKO (line)]] | wt | 118 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.371× (z -9.2) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 62.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.369× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW 1271 (line)]] | alt | 117 | 0 | 2 (1 ⚠) | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0864× (z -10.1) |
| [[SW1417 (line)]] | alt | 65.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.266× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A498 (line)]] | wt | 116 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -14.1) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 109 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.343× (z -9.1) |
| [[Hs 766T (line)]] | wt | 130 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.321× (z -10.3) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.457× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW 1088 (line)]] | alt | 174 | 0 | 1 (1 ⚠) | — | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.165× (z -8.6) ⚠ toxic |
| [[SW48 (line)]] | wt | 86.8 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.137× (z -12.0) |
| [[AN3 CA (line)]] | alt | 132 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6978), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC4]] | +0.68 | +0.58 / +0.68 | both halves | 8e-06 | STRING 435 |
| [[METTL15]] | +0.66 | +0.53 / +0.75 | both halves | 1e-05 |  |
| [[LINC01473]] | +0.64 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[GALK2]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ANKRD26]] | +0.63 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[TRMT1L]] | +0.62 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[ATG10]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[VPS13B]] | +0.60 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[TMEM260]] | +0.59 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[IMMP2L]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[CBR4]] | +0.57 | +0.63 / +0.40 | both halves | 4e-05 |  |
| [[MBD5]] | +0.57 | +0.41 / +0.67 | both halves | 4e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP295NL]] | -0.61 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[SEMA3F]] | -0.59 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[LYSMD4]] | -0.59 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[DNMT3B]] | -0.59 | -0.60 / -0.49 | both halves | 2e-05 |  |
| [[RTN4R]] | -0.59 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[ATP2A3]] | -0.58 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[RIMS3]] | -0.58 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[CROCCP3]] | -0.57 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[FAM124A]] | -0.57 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[GPRIN1]] | -0.57 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[BMP8B]] | -0.57 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[PRR5]] | -0.57 | -0.57 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.526). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-24.6, 30.0); signed map (9.4, -13.1). **Vector** length 75.9, 27.4% of its response variance represented; |z| ≥ 3 in 1,401 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +0.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +4.0 | -2.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.6 | +4.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +3.6 | -6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | -1.3 |
|  | [[Sulfatinib (drug)]] 5 µM |  | +1.7 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.5 | +3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.5 | +1.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.8 | -2.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -0.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | -5.2 | -7.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.1 | -7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -4.8 | -8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -6.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.0 | -1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.4 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain containing kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q24 — chr4:106,041,599-106,316,683 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC16169, HSPC302, Fy-1, FERRY1 |
| Gene groups (HGNC) | Pseudokinases; TBC1 domain family members; FERRY complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TEA7](https://www.uniprot.org/uniprotkb/Q8TEA7) (TBC domain-containing protein kinase-like protein):

> Component of the FERRY complex (Five-subunit Endosomal Rab5 and RNA/ribosome intermediary). The FERRY complex directly interacts with mRNAs and RAB5A, and functions as a RAB5A effector involved in the localization and the distribution of specific mRNAs most likely by mediating their endosomal transport. The complex recruits mRNAs and ribosomes to early endosomes through direct mRNA-interaction. Also involved in the modulation of mTOR signaling and expression of mTOR complex components. Involved …

**Summary**, from NCBI Gene [93627](https://www.ncbi.nlm.nih.gov/gene/93627):

> This gene encodes a protein that contains a protein kinase domain, a Rhodanase-like domain and the Tre-2/Bub2/Cdc16 (TBC) domain. The encoded protein is thought to play a role in actin organization, cell growth and cell proliferation by regulating the mammalian target of the rapamycin (mTOR) signaling pathway. This protein may also be involved in the transcriptional regulation of the components of the mTOR complex. Alternative splicing results in multiple transcript variants. [provided by …

**Accessions** — [HGNC:28261](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28261) · Entrez [93627](https://www.ncbi.nlm.nih.gov/gene/93627) · UniProt [Q8TEA7](https://www.uniprot.org/uniprotkb/Q8TEA7) · Ensembl [ENSG00000145348](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145348)

## Data

Gene col 6978: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6978); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6978, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6978]; `tensor/DDL_lfc|DDL_z.npy` [6978]; `embed/gene_vectors.npy` [6978]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6978 or target_col == 6978). Every well: [[TBCK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBCK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
