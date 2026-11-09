---
symbol: "KIF18A"
type: "gene"
col: 4282
ensembl_id: "ENSG00000121621"
name: "kinesin family member 18A"
location: "11p14.1"
module: 22
arm: "+"
pooled_cpm: 68.93
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 36
n_dd_up_clean: 1
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# KIF18A

*kinesin family member 18A* — 11p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.59× (z +19.1, q 0e+00, up in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~67% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.42× (z +5.0, q 3e-05, up in 25 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 15 lines (PANC-1 4.37×, NCI-H2347 4.91×, Panc 03.27 5.73×, RKO 8.68×, …; ⚠ cell-cycle shift, explains ~67% of this change).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (19 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.585× (z -10.7, q 4e-24, down in 41 of 47 measured lines) ⚠ cell-cycle shift, explains ~76% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.601× (z -7.2, q 6e-11, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TOP2A]] (+0.93, fdr 7e-06), [[DLGAP5]] (+0.93, fdr 7e-06), [[NDC80]] (+0.93, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NDC80]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 13 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4282.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 15 lines (PANC-1 4.37×, NCI-H2347 4.91×, Panc 03.27 5.73×, RKO 8.68×, …; ⚠ cell-cycle shift, explains ~67% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **2.59×** | +19.1 | 0e+00 | 43/47 (PANC-1, NCI-H2347, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **2.31×** | +11.9 | 5e-30 | 43/47 (A-172, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.81×** | +8.1 | 1e-13 | 38/47 (NCI-H2347, PANC-1, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.72×** | +7.7 | 2e-12 | 37/47 (A-172, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.66×** | +7.2 | 7e-11 | 36/47 (A-172, KATO III, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.61×** | +6.8 | 1e-09 | 37/47 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **1.59×** | +6.6 | 4e-09 | 35/47 (KATO III, HT-29, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.25×** | +6.0 | 1e-07 | 27/47 (HT-29, J82, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.51×** | +5.8 | 3e-07 | 36/46 (A-172, NCI-H23, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.46×** | +5.4 | 4e-06 | 25/47 (J82, A-172, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **2.02×** | +5.2 | 9e-06 | 30/46 (J82, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +5.0 | 3e-05 | 25/47 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.23×** | +4.2 | 0.001 | 23/47 (HT-29, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.29×** | +3.6 | 0.011 | 20/47 (J82, A-172, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 19 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4282.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.585×** | -10.7 | 4e-24 | 41/47 (A498, HOP62, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.537×** | -8.4 | 1e-14 | 42/47 (LS 180, A498, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.534×** | -8.2 | 4e-14 | 36/47 (C32, HT-29, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.573×** | -7.9 | 4e-13 | 36/47 (HEC-1-A, NCI-H2030, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.369×** | -7.4 | 2e-11 | 32/44 (A498, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.601×** | -7.2 | 6e-11 | 30/47 (AN3 CA, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.626×** | -6.4 | 2e-08 | 26/47 (H4, A498, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.754×** | -5.7 | 1e-06 | 29/47 (A498, H4, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.661×** | -5.6 | 1e-06 | 30/47 (A498, NCI-H1573, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.658×** | -5.5 | 2e-06 | 25/43 (SK-MEL-2, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.671×** | -5.4 | 3e-06 | 22/40 (A498, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.699×** | -5.1 | 2e-05 | 28/46 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **0.734×** | -4.2 | 0.001 | 23/46 (A549, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.760×** | -3.9 | 0.004 | 22/47 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.745×** | -3.8 | 0.004 | 19/47 (PANC-1, A549, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.696×** | -3.6 | 0.010 | 18/47 (SNU-1, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.791×** | -3.3 | 0.022 | 13/47 (SW480, NCI-H2030, …) | rises with dose | position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.718×** | -3.3 | 0.023 | 14/47 (PANC-1, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 5 µM |  | **0.794×** | -3.3 | 0.023 | 12/47 (A549, SW480, …) | rises with dose | position effect removed |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **0.797×** | -3.2 | 0.027 | 14/47 (SW 1271, SK-MEL-2, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.857× | -3.1 | 0.040 | 14/47 (HOP62, MIA PaCa-2, …) | all doses, flat |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.663×** | -3.0 | 0.045 | 14/47 (SW48, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.796×** | -3.0 | 0.050 | 16/47 (SW 1088, HOP62, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.741×** | -2.9 | 0.056 | 13/47 (HOP62, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.815×** | -2.9 | 0.062 | 16/47 (SNU-1, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.89 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4282. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 77.7 | 0 | 9 (7 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.304× (z -15.6) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.437× (z -10.8) |
| [[A-172 (line)]] | wt | 40.9 | 4 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +17.2) ⚠ cell-cycle shift, explains ~67% of this change | [[Selinexor (drug)]] 5 µM 0.359× (z -11.1) ⚠ cell-cycle shift, explains ~76% of this change |
| [[A549 (line)]] | wt | 86.4 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +14.9) ⚠ cell-cycle shift, explains ~67% of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.268× (z -9.9) ⚠ cell-cycle shift, explains ~45% of this change |
| [[C32 (line)]] | wt | 50.1 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +12.9) ⚠ cell-cycle shift, explains ~67% of this change | [[Selinexor (drug)]] 5 µM 0.314× (z -10.6) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.395× (z -8.5) |
| [[H4 (line)]] | wt | 123 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0600× (z -14.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.198× (z -12.7) |
| [[HOP62 (line)]] | alt | 113 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +12.9) ⚠ cell-cycle shift, explains ~67% of this change | [[Selinexor (drug)]] 5 µM 0.277× (z -15.4) ⚠ cell-cycle shift, explains ~76% of this change |
| [[HT-29 (line)]] | alt | 68.7 | 2 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.91× (z +9.3) ⚠ cell-cycle shift, explains ~52% of this change | [[Selinexor (drug)]] 5 µM 0.367× (z -9.7) ⚠ cell-cycle shift, explains ~76% of this change |
| [[LOX-IMVI (line)]] | wt | 110 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +10.9) ⚠ cell-cycle shift, explains ~67% of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.253× (z -10.3) ⚠ cell-cycle shift, explains ~90% of this change |
| [[KATO III (line)]] | alt | 29.6 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.59× (z +10.5) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[LoVo (line)]] | wt | 40.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.97× (z +10.8) ⚠ cell-cycle shift, explains ~52% of this change | [[Selinexor (drug)]] 5 µM 0.422× (z -9.6) ⚠ cell-cycle shift, explains ~76% of this change |
| [[LS 180 (line)]] | wt | 45.4 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.226× (z -13.0) ⚠ cell-cycle shift, explains ~76% of this change |
| [[PANC-1 (line)]] | alt | 78.4 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +19.8) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[SW480 (line)]] | alt | 114 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.433× (z -8.5) |
| [[A-427 (line)]] | wt | 115 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.416× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 107 | 0 | 2 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.318× (z -10.8) ⚠ cell-cycle shift, explains ~45% of this change |
| [[J82 (line)]] | alt | 84.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +16.7) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[NCI-H2030 (line)]] | alt | 56.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +18.7) ⚠ cell-cycle shift, explains ~67% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.311× (z -9.6) ⚠ cell-cycle shift, explains ~45% of this change |
| [[NCI-H2347 (line)]] | alt | 57.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +19.8) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[NCI-H460 (line)]] | wt | 74.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +10.4) ⚠ cell-cycle shift, explains ~67% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -13.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[Panc 03.27 (line)]] | alt | 78.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +19.8) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[RKO (line)]] | wt | 48.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.68× (z +19.2) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 64.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +15.9) ⚠ cell-cycle shift, explains ~67% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.214× (z -10.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 120 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.194× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 29.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.61× (z +14.2) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[CFPAC-1 (line)]] | alt | 30.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +10.5) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[HCT15 (line)]] | alt | 87.4 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0776× (z -11.5) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 75.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +8.7) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[HS-578T (line)]] | alt | 56.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +12.2) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 47.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +9.3) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[NCI-H1792 (line)]] | alt | 40.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +8.8) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[NCI-H661 (line)]] | alt | 68.6 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0816× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 71.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +11.3) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[SNU-423 (line)]] | alt | 89.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +10.9) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[SW1417 (line)]] | alt | 78.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +12.1) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[BT-474 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.5 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 49.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4282), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOP2A]] | +0.93 | +0.93 / +0.93 | both halves | 7e-06 | STRING 643 |
| [[DLGAP5]] | +0.93 | +0.92 / +0.92 | both halves | 7e-06 | STRING 945 |
| [[NDC80]] | +0.93 | +0.91 / +0.92 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 853 |
| [[BUB1]] | +0.92 | +0.90 / +0.92 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 865 |
| [[BIRC5]] | +0.92 | +0.91 / +0.91 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 622 |
| [[TPX2]] | +0.92 | +0.89 / +0.92 | both halves | 7e-06 | STRING 711 |
| [[KIF2C]] | +0.91 | +0.89 / +0.90 | both halves | 7e-06 | same gene group; pathway: Affinity selection of immunoglobulins; STRING 954 |
| [[CDCA8]] | +0.91 | +0.90 / +0.89 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 742 |
| [[KIF4A]] | +0.91 | +0.91 / +0.89 | both halves | 7e-06 | same gene group; pathway: Affinity selection of immunoglobulins; STRING 812 |
| [[MKI67]] | +0.90 | +0.87 / +0.91 | both halves | 7e-06 | same gene group; STRING 691 |
| [[CDK1]] | +0.90 | +0.89 / +0.88 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 843 |
| [[CCNB2]] | +0.90 | +0.88 / +0.88 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 809 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDC80]] | C | NDC80 activity raises KIF18A's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.55× lower at baseline in the lines without NDC80 | 0.014 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[FAM72D]] | C | FAM72D activity raises KIF18A's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.18× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[PBK]] | C | PBK activity raises KIF18A's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.65× lower at baseline in the lines without PBK | 0.068 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises KIF18A's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 2.80× lower at baseline in the lines without CDCA3, SPDL1 | 0.096 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.943). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.4, -56.1); signed map (-49.9, -43.2). **Vector** length 155, 57.0% of its response variance represented; |z| ≥ 3 in 1,383 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.75 to 60); *DREAM G2/M down* (control, mean cos +0.85 to 28); *E2F targets* (hallmark, mean cos +0.72 to 46).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +5.9 | +19.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +5.6 | +5.2 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.2 | +4.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | +5.0 | +5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +4.8 | +11.9 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.9 | +0.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.4 | +2.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.3 | +2.1 |
|  | [[Relugolix (drug)]] 0.5 µM |  | +2.1 | +1.7 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +2.1 | +1.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -10.0 | -7.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | -9.6 | -8.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | -8.4 | -10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.1 | -7.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -7.9 | -8.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.0 | -3.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | -5.1 | -5.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.5 | -2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 18A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p14.1 — chr11:28,020,619-28,108,156 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434G2226, PPP1R99 |
| Gene groups (HGNC) | Kinesins; Protein phosphatase 1 regulatory subunits |
| Reactome | 30 pathways, smallest: Kinesins; Processing of antigen in germinal center B cells; COPI-dependent Golgi-to-ER retrograde traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NI77](https://www.uniprot.org/uniprotkb/Q8NI77) (Kinesin-like protein KIF18A):

> Microtubule-depolymerizing kinesin which plays a role in chromosome congression by reducing the amplitude of preanaphase oscillations and slowing poleward movement during anaphase, thus suppressing chromosome movements. May stabilize the CENPE-BUB1B complex at the kinetochores during early mitosis and maintains CENPE levels at kinetochores during chromosome congression.

**Summary**, from NCBI Gene [81930](https://www.ncbi.nlm.nih.gov/gene/81930):

> KIF18A is a member of the kinesin superfamily of microtubule-associated molecular motors (see MIM 148760) that use hydrolysis of ATP to produce force and movement along microtubules (Luboshits and Benayahu, 2005 [PubMed 15878648]).[supplied by OMIM, Aug 2008]

**Accessions** — [HGNC:29441](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29441) · Entrez [81930](https://www.ncbi.nlm.nih.gov/gene/81930) · UniProt [Q8NI77](https://www.uniprot.org/uniprotkb/Q8NI77) · Ensembl [ENSG00000121621](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121621)

## Data

Gene col 4282: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4282); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4282, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4282]; `tensor/DDL_lfc|DDL_z.npy` [4282]; `embed/gene_vectors.npy` [4282]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4282 or target_col == 4282). Every well: [[KIF18A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF18A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
