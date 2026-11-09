---
symbol: "DPY19L1P1"
type: "gene"
col: 13705
ensembl_id: "ENSG00000229358"
name: "DPY19L1 pseudogene 1"
location: "7p14.3"
module: 18
arm: "+"
pooled_cpm: 78.19
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 37
n_dd_up_clean: 0
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# DPY19L1P1

*DPY19L1 pseudogene 1* — 7p14.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 2.19×, RPMI-7951 2.40×; ⚠ cell-cycle shift, explains ~40% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 1.90×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.456× (z -16.8, q 0e+00, down in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.370× (z -15.1, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPY19L2P3]] (+0.65, fdr 7e-06), [[KIF27]] (+0.63, fdr 1e-05), [[ARHGEF11]] (+0.63, fdr 1e-05); moves opposite to [[PLCD1]] (-0.59, fdr 4e-05), [[ZNF526]] (-0.57, fdr 7e-05), [[OSBPL7]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[COL6A2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13705.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 2.19×, RPMI-7951 2.40×; ⚠ cell-cycle shift, explains ~40% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 1.90×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | 1.29× | +3.7 | 0.11 | 23/47 (SW480, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13705.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.456×** | -16.8 | 0e+00 | 39/48 (HEC-1-A, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.350×** | -15.3 | 0e+00 | 44/48 (NCI-H460, A549, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.370×** | -15.1 | 0e+00 | 46/48 (C-33 A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.381×** | -14.6 | 0e+00 | 47/48 (NCI-H460, C-33 A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.464×** | -11.6 | 4e-29 | 41/48 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.477×** | -11.2 | 4e-27 | 43/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.503×** | -10.4 | 2e-23 | 41/48 (KATO III, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.511×** | -10.2 | 2e-22 | 43/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.514×** | -10.1 | 5e-22 | 37/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.285×** | -9.9 | 2e-21 | 46/49 (PANC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.532×** | -9.2 | 2e-18 | 37/47 (PANC-1, J82, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.348×** | -8.4 | 3e-15 | 37/48 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.588×** | -7.7 | 6e-13 | 28/47 (HepG2/C3A, RKO, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.647×** | -6.6 | 2e-09 | 36/48 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.635×** | -6.3 | 9e-09 | 29/44 (RKO, A549, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.629×** | -6.1 | 3e-08 | 32/48 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.586×** | -4.2 | 6e-04 | 31/48 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.825×** | -4.1 | 0.001 | 25/49 (NCI-H460, SHP-77, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.827×** | -4.0 | 0.001 | 23/48 (SNU-1, SW 1271, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.774×** | -3.8 | 0.003 | 25/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.765×** | -3.8 | 0.003 | 25/48 (HepG2/C3A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.732×** | -3.3 | 0.016 | 19/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.797×** | -3.2 | 0.023 | 20/48 (HEC-1-A, SW480, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13705. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 161 | 0 | 20 (14 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.162× (z -18.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.149× (z -17.7) |
| [[PANC-1 (line)]] | alt | 178 | 0 | 15 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -20.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.252× (z -15.5) |
| [[SW480 (line)]] | alt | 68.8 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -14.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.294× (z -14.5) |
| [[KATO III (line)]] | alt | 91.8 | 0 | 10 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.250× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.253× (z -14.3) |
| [[MIA PaCa-2 (line)]] | alt | 82.3 | 0 | 10 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.182× (z -15.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.223× (z -13.9) |
| [[A549 (line)]] | wt | 105 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -25.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.202× (z -15.1) |
| [[HepG2_C3A (line)]] | wt | 86.6 | 0 | 9 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.156× (z -15.1) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.242× (z -12.0) |
| [[NCI-H23 (line)]] | alt | 66.9 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.312× (z -11.1) |
| [[SNU-1 (line)]] | wt | 90.3 | 0 | 9 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.107× (z -16.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.171× (z -11.8) |
| [[A-427 (line)]] | wt | 80.3 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -13.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.299× (z -12.6) |
| [[HEC-1-A (line)]] | alt | 95.6 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -26.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -19.4) |
| [[LOX-IMVI (line)]] | wt | 77.0 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.204× (z -15.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.242× (z -14.5) |
| [[RKO (line)]] | wt | 66.5 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -18.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.333× (z -10.0) |
| [[COLO 205 (line)]] | alt | 111 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -21.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.188× (z -13.7) |
| [[C32 (line)]] | wt | 89.3 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.223× (z -11.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.205× (z -10.8) |
| [[HT-29 (line)]] | alt | 77.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -12.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.305× (z -11.8) |
| [[J82 (line)]] | alt | 41.6 | 0 | 5 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.288× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[SHP-77 (line)]] | alt | 91.1 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.258× (z -13.1) |
| [[SW1417 (line)]] | alt | 78.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -11.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.326× (z -10.5) |
| [[A498 (line)]] | wt | 100 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -16.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.254× (z -10.5) |
| [[C-33 A (line)]] | alt | 133 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.143× (z -17.3) |
| [[NCI-H1792 (line)]] | alt | 66.6 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.4) ⚠ cell-cycle shift, explains ~40% of this change | [[Harringtonine (drug)]] 5 µM 0.289× (z -10.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.326× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 99.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.304× (z -12.3) |
| [[A-172 (line)]] | wt | 69.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.265× (z -11.5) |
| [[AsPC-1 (line)]] | alt | 57.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -14.3) ⚠ cell-cycle shift, explains ~40% of this change |
| [[LoVo (line)]] | wt | 57.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.382× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.405× (z -9.6) |
| [[LS 180 (line)]] | wt | 43.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -10.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW48 (line)]] | wt | 70.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -10.6) |
| [[AN3 CA (line)]] | alt | 72.1 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.116× (z -11.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.163× (z -9.7) |
| [[BT-474 (line)]] | alt | 46.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -12.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[HOP62 (line)]] | alt | 40.8 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.310× (z -10.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H2030 (line)]] | alt | 95.6 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.313× (z -9.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.367× (z -8.5) |
| [[SNU-423 (line)]] | alt | 55.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -10.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.276× (z -10.5) |
| [[SW 900 (line)]] | alt | 49.8 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.236× (z -10.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[CHP-212 (line)]] | wt | 31.9 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0854× (z -9.0) ⚠ cell-cycle shift, explains ~53% of this change |
| [[H4 (line)]] | wt | 85.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -11.0) ⚠ cell-cycle shift, explains ~40% of this change |
| [[HCT15 (line)]] | alt | 54.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[Hs 766T (line)]] | wt | 43.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[NCI-H1573 (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.291× (z -9.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[Panc 03.27 (line)]] | alt | 57.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[RPMI-7951 (line)]] | alt | 40.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +8.6) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[SW 1271 (line)]] | alt | 84.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.116× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 81.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13705), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPY19L2P3]] | +0.65 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[KIF27]] | +0.63 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[ARHGEF11]] | +0.63 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[SPOPL-DT]] | +0.62 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[ATE1]] | +0.60 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[ARID2]] | +0.60 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[ZNRF2P2]] | +0.60 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[JADE3]] | +0.60 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[PKD2]] | +0.59 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[NR2C2]] | +0.59 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[ENOX2]] | +0.58 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[PRMT3]] | +0.57 | +0.57 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLCD1]] | -0.59 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[ZNF526]] | -0.57 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[OSBPL7]] | -0.57 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[RAB3A]] | -0.55 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[NAGK]] | -0.54 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[ATOSB]] | -0.54 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[PLXNA3]] | -0.54 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[STRA6LP]] | -0.52 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[TMEM92-AS1]] | -0.52 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[EHD2]] | -0.52 | -0.50 / -0.37 | both halves | 7e-05 |  |
| [[KLHL26]] | -0.52 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[RCN3]] | -0.52 | -0.47 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL6A2]] | B | COL6A2 activity lowers DPY19L1P1's level | lines that do not express COL6A2 (28) vs lines expressing it (22) | 1.33× higher at baseline in the lines without COL6A2 | 0.099 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.386). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-7.3, 13.6); signed map (7.5, -4.3). **Vector** length 80.4, 23.9% of its response variance represented; |z| ≥ 3 in 1,260 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.9 | +2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +3.9 | -6.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +3.6 | -4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +3.4 | -10.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.3 | +0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | -3.8 |
|  | [[Acetohexamide (drug)]] 5 µM |  | +1.4 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | -1.9 |
|  | [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | +1.2 | +1.7 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.9 | -4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.6 | -15.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.4 | -14.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | -4.1 | -5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -10.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | -1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -8.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | DPY19L1 pseudogene 1 |
| Locus type | pseudogene |
| Location | 7p14.3 — chr7:32,580,949-32,761,787 (-) |
| Ensembl biotype | unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:22395](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22395) · Entrez [100129460](https://www.ncbi.nlm.nih.gov/gene/100129460) · Ensembl [ENSG00000229358](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229358)

## Data

Gene col 13705: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13705); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13705, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13705]; `tensor/DDL_lfc|DDL_z.npy` [13705]; `embed/gene_vectors.npy` [13705]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13705 or target_col == 13705). Every well: [[DPY19L1P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPY19L1P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
