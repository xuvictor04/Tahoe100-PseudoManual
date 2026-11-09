---
symbol: "GLI2"
type: "gene"
col: 1067
ensembl_id: "ENSG00000074047"
name: "GLI family zinc finger 2"
location: "2q14.2"
module: 195
arm: "+"
pooled_cpm: 43.99
n_lines_expressing: 37
n_dd_up: 1
n_dd_down: 31
n_dd_up_clean: 1
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/195"]
generated_by: "tahoemap"
---

# GLI2

*GLI family zinc finger 2* — 2q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.33× (z +4.0, q 0.035, up in 12 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 2 lines (SW480 2.25×, HEC-1-A 2.42×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (NCI-H460 2.50×); [[Daptomycin (drug)]] 5 µM in 1 line (NCI-H460 3.10×; ⚠ unreliable plate only); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (NCI-H460 2.99×).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.326× (z -15.9, q 0e+00, down in 27 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.367× (z -14.3, q 1e-43, down in 34 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IGSF9B]] (+0.62, fdr 1e-05), [[OAF]] (+0.57, fdr 1e-05), [[MGAT5B]] (+0.57, fdr 1e-05); moves opposite to [[C11orf54]] (-0.52, fdr 3e-05), [[DAZAP2]] (-0.51, fdr 5e-05), [[ATP6V1C1]] (-0.49, fdr 7e-05).
> It is in [[Module 195]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAMLD1]] → it (grade B ⚠); 2 go from it, the strongest it → [[MAMLD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1067.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 2 lines (SW480 2.25×, HEC-1-A 2.42×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (NCI-H460 2.50×); [[Daptomycin (drug)]] 5 µM in 1 line (NCI-H460 3.10×; ⚠ unreliable plate only); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (NCI-H460 2.99×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +4.0 | 0.035 | 12/35 (SW480, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.2 | 0.45 | 14/35 (SW480, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1067.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.326×** | -15.9 | 0e+00 | 27/33 (SNU-1, SW48, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.367×** | -14.3 | 1e-43 | 34/35 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.395×** | -12.7 | 1e-34 | 26/32 (NCI-H2030, A-427, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.389×** | -12.4 | 3e-33 | 24/33 (Hs 766T, H4, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.569×** | -11.3 | 1e-27 | 24/35 (HOP62, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.460×** | -11.0 | 3e-26 | 29/34 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.546×** | -8.6 | 7e-16 | 27/35 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.554×** | -8.4 | 3e-15 | 25/34 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.542×** | -8.4 | 4e-15 | 23/34 (J82, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.699×** | -7.2 | 3e-11 | 24/35 (A-427, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.608×** | -7.1 | 8e-11 | 26/35 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.614×** | -6.9 | 2e-10 | 26/35 (A498, Hs 766T, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.430×** | -6.3 | 2e-08 | 23/35 (LoVo, HOP62, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.486×** | -5.4 | 3e-06 | 22/33 (Hs 766T, AsPC-1, …) | top dose only | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.695×** | -5.2 | 8e-06 | 22/35 (LoVo, SNU-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.734×** | -4.4 | 4e-04 | 18/35 (SNU-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.746×** | -4.2 | 9e-04 | 19/35 (AN3 CA, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Sulfatinib (drug)]] 5 µM |  | **0.747×** | -4.0 | 0.002 | 20/35 (HOP62, J82, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.608×** | -3.7 | 0.006 | 16/34 (HCT15, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.840× | -3.5 | 0.011 | 14/35 (NCI-H460, J82, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.648×** | -3.5 | 0.013 | 14/35 (AsPC-1, Panc 03.27, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1067. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 47.9 | 4 (2 ⚠) | 13 (8 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.50× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -22.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -18.0) |
| [[HOP62 (line)]] | alt | 93.0 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -23.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.125× (z -16.5) |
| [[SNU-1 (line)]] | wt | 576 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -22.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -14.2) |
| [[LoVo (line)]] | wt | 124 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -23.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.107× (z -19.4) |
| [[Hs 766T (line)]] | wt | 77.9 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0191× (z -26.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.252× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 47.4 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0444× (z -26.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.242× (z -12.5) |
| [[HS-578T (line)]] | alt | 63.4 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0682× (z -22.9) |
| [[hTERT-HPNE (line)]] | wt | 110 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0982× (z -12.1) |
| [[J82 (line)]] | alt | 29.4 | 0 | 5 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0998× (z -14.0) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -11.7) |
| [[A-427 (line)]] | wt | 60.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.241× (z -13.7) |
| [[A549 (line)]] | wt | 95.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -16.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.328× (z -9.7) |
| [[AN3 CA (line)]] | alt | 136 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0647× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.176× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 37.9 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.156× (z -12.9) |
| [[PANC-1 (line)]] | alt | 53.2 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -15.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 87.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.337× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 24.4 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -9.6) |
| [[SW48 (line)]] | wt | 84.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0824× (z -16.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 22.4 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.25× (z +9.1) | [[Docetaxel (drug)]] 0.05 µM 0.263× (z -10.7) ⚠ transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.298× (z -9.7) |
| [[C-33 A (line)]] | alt | 53.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.258× (z -9.3) |
| [[CHP-212 (line)]] | wt | 122 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.100× (z -11.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 71.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0638× (z -17.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 35.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.160× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 28.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +9.2) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -11.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 31.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -8.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 27.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.42× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 31.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -9.0) |
| [[LS 180 (line)]] | wt | 34.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.184× (z -9.9) |
| [[NCI-H661 (line)]] | alt | 46.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0443× (z -10.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 22.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -10.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[BT-474 (line)]] | alt | 5.31 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.15 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.72 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.59 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.69 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.57 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.51 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.09 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.24 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.77 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.04 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.49 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1067), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGSF9B]] | +0.62 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[OAF]] | +0.57 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[MGAT5B]] | +0.57 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[CDYL2]] | +0.56 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[VAV2]] | +0.56 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[PLEKHG5]] | +0.55 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[PRR5]] | +0.55 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[MPZL1]] | +0.53 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[CPA6]] | +0.52 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[MPP3]] | +0.52 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[KCNC4]] | +0.52 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[ANO1]] | +0.51 | +0.46 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf54]] | -0.52 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[DAZAP2]] | -0.51 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[ATP6V1C1]] | -0.49 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[C21orf62-AS1]] | -0.49 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[LINC02889]] | -0.48 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[N4BP2L2]] | -0.47 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[PPP4R3B]] | -0.47 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[GTF2IRD2B]] | -0.47 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[GTF2IRD2]] | -0.46 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[SPATA24]] | -0.45 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[RRAGC-DT]] | -0.45 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[PPP1R3E]] | -0.45 | -0.41 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAMLD1]] | B | MAMLD1 activity raises GLI2's level | lines that do not express MAMLD1 (11) vs lines expressing it (39) | 2.42× lower at baseline in the lines without MAMLD1 | 0.057 | ⚠ within organs, on part of the lines; also absent: FHOD3, PGM5P2-1, CAV1 |
| [[TCF7L1]] | B | TCF7L1 activity raises GLI2's level | lines that do not express TCF7L1 (12) vs lines expressing it (38) | 2.20× lower at baseline in the lines without TCF7L1 | 0.080 | ⚠ within organs, on part of the lines; also absent: EML1, PYGO1, FAM124A |
| [[TLN2]] | B | TLN2 activity raises GLI2's level | lines that do not express TLN2 (5) vs lines expressing it (45) | 3.38× lower at baseline in the lines without TLN2 | 0.085 | ⚠ within organs, on part of the lines; also absent: FAT3, ENSG00000232732, SLC26A2; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAMLD1]] | B | GLI2 activity raises MAMLD1's level | lines that do not express GLI2 (13) vs lines expressing it (37) | 2.40× lower at baseline in the lines without GLI2 | 0.047 | ⚠ within organs, on part of the lines; also absent: HAPLN3 |
| [[KCNC4]] | B | GLI2 activity strengthens KCNC4's drug response | lines that do not express GLI2 (10) vs lines expressing it (32) | the lines without GLI2 respond 0.54× as strongly (z diff +1.91); strongest at Ouabain (Octahydrate) 0.5 µM: 0.85x vs 0.50x (z diff +3.0) | 0.080 | ⚠ within organs, on part of the lines; also absent: HAPLN3; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 195]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (50.5, -0.5); signed map (-0.1, 53.4). **Vector** length 110, 29.7% of its response variance represented; |z| ≥ 3 in 1,088 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.0 | +2.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.4 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.3 | +4.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.7 | +0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | -1.8 |
|  | [[vincristine (drug)]] 5 µM |  | +1.7 | +1.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.4 | -14.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.1 | -8.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.0 | -7.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.8 | -6.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.7 | -6.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.3 | -2.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -3.1 | -2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.7 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | GLI family zinc finger 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.2 — chr2:120,735,623-120,992,653 (+) |
| Ensembl biotype | protein_coding |
| Also known as | THP2, HPE9, THP1 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Reactome | 8 pathways, smallest: RUNX2 regulates chondrocyte maturation; GLI proteins bind promoters of Hh responsive genes to promote transcription; RUNX2 regulates bone development |
| Matched by | ensembl_id |

**Function**, from UniProt [P10070](https://www.uniprot.org/uniprotkb/P10070) (Transcription activator GLI2):

> Transcription factor that acts as a key effector of the smoothened signaling pathway, and which plays a role in skeleton development. Specifically binds to the minimal GLI-consensus sequence 5'-GACCACCCA-3' to activate or repress the expression of target genes (By similarity). Functions both as a transcriptional activator and repressor: the full-length GLI2 form (Transcription activator GLI2) acts as a transcription activator following smoothened activation, while the Transcription repressor …

**Summary**, from NCBI Gene [2736](https://www.ncbi.nlm.nih.gov/gene/2736):

> This gene encodes a protein which belongs to the C2H2-type zinc finger protein subclass of the Gli family. Members of this subclass are characterized as transcription factors which bind DNA through zinc finger motifs. These motifs contain conserved H-C links. Gli family zinc finger proteins are mediators of Sonic hedgehog (Shh) signaling and they are implicated as potent oncogenes in the embryonal carcinoma cell. The protein encoded by this gene localizes to the cytoplasm and activates patched …

**Accessions** — [HGNC:4318](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4318) · Entrez [2736](https://www.ncbi.nlm.nih.gov/gene/2736) · UniProt [P10070](https://www.uniprot.org/uniprotkb/P10070) · Ensembl [ENSG00000074047](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074047)

## Data

Gene col 1067: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1067); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1067, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1067]; `tensor/DDL_lfc|DDL_z.npy` [1067]; `embed/gene_vectors.npy` [1067]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1067 or target_col == 1067). Every well: [[GLI2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLI2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
