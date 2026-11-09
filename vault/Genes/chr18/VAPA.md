---
symbol: "VAPA"
type: "gene"
col: 2153
ensembl_id: "ENSG00000101558"
name: "VAMP associated protein A"
location: "18p11.22"
module: 17
arm: "+"
pooled_cpm: 176.39
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# VAPA

*VAMP associated protein A* — 18p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.34× (z +19.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.686× (z -12.1, q 1e-30, down in 36 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 10 lines (NCI-H460 0.418×, SW 900 0.447×, A549 0.467×, HOP62 0.495×, …); [[Panobinostat (drug)]] 5 µM in 4 lines (NCI-H460 0.390×, PANC-1 0.449×, MIA PaCa-2 0.365×, SW 900 0.361×; ⚠ cell-cycle shift, explains ~26% of this change); [[Belinostat (drug)]] 5 µM in 4 lines (PANC-1 0.488×, NCI-H460 0.484×, MIA PaCa-2 0.421×, SW 900 0.396×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.610×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WAC]] (+0.72, fdr 7e-06), [[RBM33]] (+0.68, fdr 7e-06), [[KCTD3]] (+0.66, fdr 7e-06); moves opposite to [[KCTD5]] (-0.69, fdr 7e-06), [[DPP9]] (-0.62, fdr 2e-05), [[MROH1]] (-0.59, fdr 4e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2153.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.34×** | +19.2 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +16.8 | 0e+00 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.02×** | +16.4 | 0e+00 | 48/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.54×** | +13.8 | 7e-41 | 39/48 (PANC-1, NCI-H23, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.92×** | +12.7 | 1e-34 | 46/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.74×** | +12.5 | 4e-34 | 39/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.72×** | +12.3 | 1e-32 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +10.3 | 4e-23 | 40/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.56×** | +9.7 | 2e-20 | 34/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.37×** | +7.1 | 7e-11 | 32/48 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.28×** | +5.4 | 4e-06 | 25/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +5.2 | 9e-06 | 24/38 (NCI-H1573, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.24×** | +4.6 | 2e-04 | 24/45 (PANC-1, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +4.5 | 2e-04 | 24/48 (PANC-1, LS 180, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.19× | +3.9 | 0.004 | 23/48 (A-427, A549, …) | rises with dose |  |
| [[Asciminib (drug)]] 0.05 µM |  | 1.16× | +3.2 | 0.038 | 13/48 (NCI-H1573, SW 900, …) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.16× | +3.2 | 0.040 | 14/49 (SNU-423, PANC-1, …) | top dose only | plate-row cell shift |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.042 | 14/48 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2153.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 10 lines (NCI-H460 0.418×, SW 900 0.447×, A549 0.467×, HOP62 0.495×, …); [[Panobinostat (drug)]] 5 µM in 4 lines (NCI-H460 0.390×, PANC-1 0.449×, MIA PaCa-2 0.365×, SW 900 0.361×; ⚠ cell-cycle shift, explains ~26% of this change); [[Belinostat (drug)]] 5 µM in 4 lines (PANC-1 0.488×, NCI-H460 0.484×, MIA PaCa-2 0.421×, SW 900 0.396×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.610×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.686×** | -12.1 | 1e-30 | 36/49 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.610×** | -11.2 | 1e-26 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.626×** | -10.6 | 5e-24 | 42/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.665×** | -9.2 | 4e-18 | 42/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.680×** | -8.4 | 6e-15 | 32/44 (LS 180, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.803×** | -4.8 | 2e-04 | 26/50 (NCI-H460, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.816×** | -4.6 | 4e-04 | 26/49 (RKO, BT-474, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.812×** | -4.6 | 4e-04 | 25/48 (SW 900, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.822×** | -4.3 | 0.001 | 25/48 (NCI-H460, SW 900, …) | top dose only |  |
| [[Ranolazine (drug)]] 0.05 µM |  | 0.847× | -3.6 | 0.014 | 16/48 (CHP-212, HOP62, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.892× | -3.6 | 0.014 | 11/48 (HOP62, A-172, …) | top dose only |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.854× | -3.6 | 0.017 | 18/48 (HOP62, NCI-H2347, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | 0.862× | -3.4 | 0.034 | 16/48 (RKO, HEC-1-A, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.871× | -3.1 | 0.069 | 12/48 (NCI-H460, SW 900, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.871× | -3.1 | 0.069 | 14/48 (HepG2/C3A, MIA PaCa-2, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.872× | -3.1 | 0.070 | 17/48 (Panc 03.27, HS-578T, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.877× | -3.0 | 0.096 | 10/48 (RPMI-7951, HEC-1-A, …) | top dose only |  |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.878× | -3.0 | 0.096 | 15/48 (HEC-1-A, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2153. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 180 | 12 (7 ⚠) | 7 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.99× (z +23.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -20.6) |
| [[PANC-1 (line)]] | alt | 168 | 11 (5 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.54× (z +24.2) | [[Panobinostat (drug)]] 5 µM 0.449× (z -15.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.488× (z -13.7) |
| [[HOP62 (line)]] | alt | 321 | 9 (3 ⚠) | 4 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.91× (z +14.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +14.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -13.8) |
| [[SW480 (line)]] | alt | 155 | 10 (5 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +23.5) | [[Panobinostat (drug)]] 5 µM 0.621× (z -10.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.649× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 166 | 10 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.26× (z +19.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.82× (z +18.9) | — |
| [[SW 900 (line)]] | alt | 235 | 5 (1 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -14.1) |
| [[BT-474 (line)]] | alt | 274 | 5 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.442× (z -11.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H23 (line)]] | alt | 204 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +18.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +13.2) | — |
| [[A-427 (line)]] | wt | 228 | 7 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +14.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.62× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.544× (z -9.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HT-29 (line)]] | alt | 250 | 5 (2 ⚠) | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.45× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.638× (z -9.0) |
| [[LS 180 (line)]] | wt | 196 | 7 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.67× (z +20.3) | [[Dinaciclib (drug)]] 5 µM 0.364× (z -12.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 194 | 5 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.44× (z +12.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.27× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.365× (z -13.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.421× (z -11.7) |
| [[A549 (line)]] | wt | 142 | 4 (3 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +15.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.34× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -14.0) |
| [[KATO III (line)]] | alt | 192 | 5 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.08× (z +20.8) | [[Panobinostat (drug)]] 5 µM 0.501× (z -10.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.560× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 136 | 6 (3 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 3.49× (z +14.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 189 | 4 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.477× (z -9.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[J82 (line)]] | alt | 157 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +12.1) | — |
| [[LoVo (line)]] | wt | 141 | 6 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.98× (z +15.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +14.4) | — |
| [[LOX-IMVI (line)]] | wt | 175 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +12.0) | — |
| [[RKO (line)]] | wt | 173 | 4 (1 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.80× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 184 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +13.5) | [[Panobinostat (drug)]] 0.5 µM 0.465× (z -8.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[H4 (line)]] | wt | 129 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.12× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 3.10× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 218 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +11.5) | — |
| [[SW48 (line)]] | wt | 121 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.61× (z +13.2) | — |
| [[A498 (line)]] | wt | 120 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +15.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.45× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.610× (z -8.7) |
| [[COLO 205 (line)]] | alt | 116 | 4 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.10× (z +11.2) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 6.72× (z +10.3) | — |
| [[HEC-1-A (line)]] | alt | 157 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 5.12× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.445× (z -8.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 130 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +14.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.77× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.622× (z -8.9) |
| [[SW1417 (line)]] | alt | 198 | 3 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.437× (z -9.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 146 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +14.5) ⚠ cell-cycle shift, explains ~33% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.634× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 220 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.449× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 194 | 0 | 3 | — | [[Bimiralisib (drug)]] 5 µM 0.181× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 238 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 3.99× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -10.3) |
| [[C-33 A (line)]] | alt | 122 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.55× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +9.1) | — |
| [[C32 (line)]] | wt | 153 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 10.1× (z +11.3) | — |
| [[HCT15 (line)]] | alt | 167 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.30× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 161 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.46× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 140 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +11.9) ⚠ cell-cycle shift, explains ~33% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -10.2) |
| [[CHP-212 (line)]] | wt | 192 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -9.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 190 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 152 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 170 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.62× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 110 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +8.9) | — |
| [[SNU-1 (line)]] | wt | 210 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.46× (z +9.1) | — |
| [[SW 1088 (line)]] | alt | 180 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[AN3 CA (line)]] | alt | 185 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 381 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 134 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2153), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WAC]] | +0.72 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[RBM33]] | +0.68 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[KCTD3]] | +0.66 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[MIER1]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[HIF1A]] | +0.64 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[TAB2]] | +0.63 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[ALDH3B1]] | +0.62 | +0.58 / +0.57 | both halves | 8e-06 | pathway: Sphingolipid metabolism |
| [[PUM2]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[CDC73]] | +0.61 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[RDX]] | +0.60 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[PRKAA1]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[CHASERR]] | +0.60 | +0.62 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD5]] | -0.69 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[DPP9]] | -0.62 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[MROH1]] | -0.59 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[MAD1L1]] | -0.59 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[ZCCHC17]] | -0.57 | -0.36 / -0.61 | both halves | 1e-04 |  |
| [[MYO9B]] | -0.57 | -0.39 / -0.60 | both halves | 6e-05 |  |
| [[GAN]] | -0.56 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[BLZF1]] | -0.56 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[TOP3A]] | -0.56 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[PDCD6]] | -0.55 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[RABGEF1]] | -0.55 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[SENP5]] | -0.55 | -0.43 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises VAPA's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises VAPA's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.410). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-17.7, 0.6); signed map (29.8, -24.2). **Vector** length 99.5, 35.6% of its response variance represented; |z| ≥ 3 in 1,294 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.8 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +7.6 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.6 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +6.0 | -4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | -8.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.1 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.1 | -0.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.7 | +1.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.7 | +0.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.6 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.3 | +3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.1 | +0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.9 | -3.1 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.4 | +0.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.4 | -1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.1 | -0.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.8 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | +4.5 |

## What is on record

|  |  |
|---|---|
| Name | VAMP associated protein A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.22 — chr18:9,914,016-9,960,021 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hVAP-33, VAP-A |
| Gene groups (HGNC) | Motile sperm domain containing |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 12 pathways, smallest: Competing endogenous RNAs (ceRNAs) regulate PTEN translation; Regulation of PTEN mRNA translation; Insertion of tail-anchored proteins into the endoplasmic reticulum membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0L0](https://www.uniprot.org/uniprotkb/Q9P0L0) (Vesicle-associated membrane protein-associated protein A):

> Endoplasmic reticulum (ER)-anchored protein that mediates the formation of contact sites between the ER and endosomes via interaction with FFAT motif-containing proteins such as STARD3 or WDR44. STARD3-VAPA interaction enables cholesterol transfer from the ER to endosomes. Via interaction with WDR44 participates in neosynthesized protein export. In addition, recruited to the plasma membrane through OSBPL3 binding. The OSBPL3-VAPA complex stimulates RRAS signaling which in turn attenuates …

**Summary**, from NCBI Gene [9218](https://www.ncbi.nlm.nih.gov/gene/9218):

> The protein encoded by this gene is a type IV membrane protein. It is present in the plasma membrane and intracellular vesicles. It may also be associated with the cytoskeleton. This protein may function in vesicle trafficking, membrane fusion, protein complex assembly and cell motility. Alternative splicing occurs at this locus and two transcript variants encoding distinct isoforms have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12648](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12648) · Entrez [9218](https://www.ncbi.nlm.nih.gov/gene/9218) · UniProt [Q9P0L0](https://www.uniprot.org/uniprotkb/Q9P0L0) · Ensembl [ENSG00000101558](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101558)

## Data

Gene col 2153: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2153); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2153, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2153]; `tensor/DDL_lfc|DDL_z.npy` [2153]; `embed/gene_vectors.npy` [2153]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2153 or target_col == 2153). Every well: [[VAPA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VAPA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
