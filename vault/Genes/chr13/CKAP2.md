---
symbol: "CKAP2"
type: "gene"
col: 5813
ensembl_id: "ENSG00000136108"
name: "cytoskeleton associated protein 2"
location: "13q14.3"
module: 22
arm: "+"
pooled_cpm: 95.31
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CKAP2

*cytoskeleton associated protein 2* — 13q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.81× (z +10.3, q 2e-22, up in 38 of 48 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Docetaxel (drug)]] 5 µM: 1.23× (z +3.7, q 0.019, up in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (Panc 03.27 4.30×, RKO 4.29×, PANC-1 2.73×, NCI-H2347 3.08×, …; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (KATO III 5.39×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (KATO III 4.59×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (11 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.668× (z -7.0, q 1e-09, down in 32 of 48 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.678× (z -4.8, q 2e-04, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEK2]] (+0.94, fdr 7e-06), [[DLGAP5]] (+0.92, fdr 7e-06), [[CENPE]] (+0.92, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[NEURL1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5813.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (Panc 03.27 4.30×, RKO 4.29×, PANC-1 2.73×, NCI-H2347 3.08×, …; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (KATO III 5.39×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (KATO III 4.59×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.81×** | +10.3 | 2e-22 | 38/48 (Panc 03.27, RKO, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~92% of this change | **1.76×** | +7.0 | 8e-10 | 40/48 (HT-29, PANC-1, …) | all doses, flat | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.76×** | +6.7 | 4e-09 | 39/48 (PANC-1, NCI-H2347, …) | rises with dose | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **2.71×** | +6.4 | 2e-08 | 40/47 (J82, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.38×** | +5.7 | 2e-06 | 42/48 (NCI-H23, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.43×** | +4.4 | 9e-04 | 34/48 (HT-29, NCI-H2030, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.019 | 24/48 (HT-29, PANC-1, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.33×** | +3.5 | 0.031 | 24/48 (KATO III, PANC-1, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.32×** | +3.4 | 0.037 | 22/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.32×** | +3.4 | 0.039 | 24/48 (KATO III, PANC-1, …) | all doses, flat | composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.31×** | +3.3 | 0.045 | 24/48 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.30×** | +3.3 | 0.054 | 24/47 (LOX-IMVI, SW 900, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **1.29×** | +3.2 | 0.063 | 21/48 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5813.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.668×** | -7.0 | 1e-09 | 32/48 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.672×** | -6.9 | 1e-09 | 33/48 (A498, SNU-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.593×** | -6.4 | 3e-08 | 34/48 (LOX-IMVI, H4, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.600×** | -6.3 | 5e-08 | 38/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.653×** | -5.0 | 5e-05 | 40/48 (NCI-H1573, NCI-H661, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.678×** | -4.8 | 2e-04 | 33/48 (NCI-H2030, A-427, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.679×** | -4.8 | 2e-04 | 33/48 (SNU-1, NCI-H1573, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.690×** | -4.5 | 4e-04 | 25/48 (LOX-IMVI, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.696×** | -4.4 | 5e-04 | 33/48 (A549, SW48, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **0.728×** | -3.9 | 0.005 | 30/48 (A-427, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.570×** | -3.6 | 0.016 | 26/48 (SW48, A498, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.749×** | -3.5 | 0.019 | 22/48 (A-172, NCI-H1573, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.754×** | -3.5 | 0.022 | 22/48 (SNU-1, H4, …) | two highest doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.819×** | -3.5 | 0.022 | 27/48 (SW1417, SW 900, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +1.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5813. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 107 | 1 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.276× (z -11.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.259× (z -8.7) |
| [[SNU-1 (line)]] | wt | 137 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0788× (z -14.5) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 81.3 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.39× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[LS 180 (line)]] | wt | 80.1 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -9.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[PANC-1 (line)]] | alt | 92.4 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +13.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 132 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.319× (z -15.4) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 99.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +12.3) ⚠ cell-cycle shift, would explain all of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.280× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 136 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.4) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -8.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HT-29 (line)]] | alt | 120 | 1 (1 ⚠) | 1 (1 ⚠) | [[Docetaxel (drug)]] 0.05 µM 3.42× (z +8.7) ⚠ transcription drop; cell-cycle shift, explains ~92% of this change | [[Lonafarnib (drug)]] 5 µM 0.0568× (z -10.6) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 82.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +13.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 99.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +16.2) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.397× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 90.6 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.344× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 96.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.318× (z -13.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 64.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +12.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 171 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -14.9) ⚠ cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 79.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.109× (z -8.6) ⚠ cell-cycle shift, explains ~82% of this change |
| [[H4 (line)]] | wt | 85.7 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.131× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 71.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +11.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[hTERT-HPNE (line)]] | wt | 79.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[J82 (line)]] | alt | 136 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 144 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -9.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H1573 (line)]] | alt | 70.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 55.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +12.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 85.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +15.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 124 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +11.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW1417 (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW48 (line)]] | wt | 124 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.280× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 114 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 124 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 57.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 58.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 261 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 170 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5813), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEK2]] | +0.94 | +0.93 / +0.94 | both halves | 7e-06 | STRING 781 |
| [[DLGAP5]] | +0.92 | +0.92 / +0.91 | both halves | 7e-06 | STRING 838 |
| [[CENPE]] | +0.92 | +0.89 / +0.92 | both halves | 7e-06 | STRING 831 |
| [[CCNB2]] | +0.92 | +0.90 / +0.92 | both halves | 7e-06 | STRING 578 |
| [[CDKN3]] | +0.92 | +0.91 / +0.90 | both halves | 7e-06 | STRING 446 |
| [[CENPF]] | +0.91 | +0.90 / +0.91 | both halves | 7e-06 | STRING 934 |
| [[TOP2A]] | +0.90 | +0.93 / +0.87 | both halves | 7e-06 | STRING 898 |
| [[NDC80]] | +0.89 | +0.88 / +0.90 | both halves | 7e-06 | STRING 743 |
| [[KIF18A]] | +0.89 | +0.89 / +0.87 | both halves | 7e-06 | STRING 455 |
| [[CCNB1]] | +0.89 | +0.89 / +0.89 | both halves | 7e-06 | STRING 682 |
| [[CKAP2L]] | +0.88 | +0.86 / +0.87 | both halves | 7e-06 |  |
| [[CCNA2]] | +0.88 | +0.85 / +0.88 | both halves | 7e-06 | STRING 781 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEURL1B]] | B | NEURL1B activity raises CKAP2's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 2.00× lower at baseline in the lines without NEURL1B | 0.010 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[PIMREG]] | B | PIMREG activity raises CKAP2's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.95× lower at baseline in the lines without PIMREG | 0.082 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises CKAP2's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 3.00× lower at baseline in the lines without NDC80 | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises CKAP2's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.73× lower at baseline in the lines without AURKB | 0.049 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[SKA3]] | C | SKA3 activity raises CKAP2's level | lines that do not express SKA3 (3) vs lines expressing it (47) | 3.42× lower at baseline in the lines without SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p |
| [[FAM72D]] | C | FAM72D activity raises CKAP2's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.01× lower at baseline in the lines without FAM72D | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.911). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.5, -57.0); signed map (-50.7, -42.9). **Vector** length 166, 64.8% of its response variance represented; |z| ≥ 3 in 1,160 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.73 to 60); *DREAM G2/M down* (control, mean cos +0.84 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.70 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +8.6 | +10.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +7.6 | +6.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~92% of this change | +6.7 | +7.0 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +5.7 | +5.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.1 | +6.7 |
|  | [[Docetaxel (drug)]] 5 µM |  | +4.0 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +3.0 | +3.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | +3.0 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +1.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.9 | -6.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.7 | -6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.6 | -4.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.8 | -7.0 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | -5.6 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -2.1 |
|  | [[EX229 (drug)]] 5 µM |  | -4.8 | -3.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.1 | -2.5 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -3.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | cytoskeleton associated protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.3 — chr13:52,455,429-52,476,628 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LB1, FLJ10749, se20-10, TMAP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WWK9](https://www.uniprot.org/uniprotkb/Q8WWK9) (Cytoskeleton-associated protein 2):

> Possesses microtubule stabilizing properties. Involved in regulating aneuploidy, cell cycling, and cell death in a p53/TP53-dependent manner (By similarity).

**Summary**, from NCBI Gene [26586](https://www.ncbi.nlm.nih.gov/gene/26586):

> This gene encodes a cytoskeleton-associated protein that stabalizes microtubules and plays a role in the regulation of cell division. The encoded protein is itself regulated through phosphorylation at multiple serine and threonine residues. There is a pseudogene of this gene on chromosome 14. Alternative splicing results in multiple transcript variations. [provided by RefSeq, Nov 2013]

**Accessions** — [HGNC:1990](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1990) · Entrez [26586](https://www.ncbi.nlm.nih.gov/gene/26586) · UniProt [Q8WWK9](https://www.uniprot.org/uniprotkb/Q8WWK9) · Ensembl [ENSG00000136108](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136108)

## Data

Gene col 5813: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5813); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5813, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5813]; `tensor/DDL_lfc|DDL_z.npy` [5813]; `embed/gene_vectors.npy` [5813]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5813 or target_col == 5813). Every well: [[CKAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CKAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
