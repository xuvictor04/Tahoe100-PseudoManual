---
symbol: "MEMO1"
type: "gene"
col: 8605
ensembl_id: "ENSG00000162959"
name: "mediator of cell motility 1"
location: "2p22.3"
module: 210
arm: "+"
pooled_cpm: 176.64
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/210"]
generated_by: "tahoemap"
---

# MEMO1

*mediator of cell motility 1* — 2p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.65× (z +17.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.334× (z -20.0, q 0e+00, down in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.532× (z -11.5, q 2e-28, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGEF11]] (+0.59, fdr 3e-05), [[MAST2]] (+0.59, fdr 1e-05), [[CHD7]] (+0.57, fdr 3e-05); moves opposite to [[UBE4A]] (-0.62, fdr 1e-05), [[RTF2]] (-0.60, fdr 4e-05), [[ZNF17]] (-0.59, fdr 3e-05).
> It is in [[Module 210]], a single-armed module (tRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8605.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.65×** | +17.7 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.37×** | +15.7 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.12×** | +13.7 | 2e-40 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.02×** | +12.8 | 2e-35 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.57×** | +8.2 | 3e-14 | 46/48 (CFPAC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +8.1 | 4e-14 | 41/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +6.8 | 7e-10 | 28/48 (CFPAC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.41×** | +6.2 | 4e-08 | 33/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.32×** | +5.1 | 2e-05 | 33/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +4.5 | 3e-04 | 28/48 (SW 900, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +4.4 | 5e-04 | 31/48 (RPMI-7951, HCT15, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +4.2 | 0.001 | 30/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.038 | 24/48 (A498, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.074 | 14/48 (J82, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8605.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.334×** | -20.0 | 0e+00 | 48/49 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.364×** | -17.7 | 0e+00 | 44/44 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.471×** | -12.7 | 2e-34 | 39/45 (LOX-IMVI, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.532×** | -11.5 | 2e-28 | 43/48 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.557×** | -10.7 | 2e-24 | 39/48 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.667×** | -7.4 | 2e-11 | 40/48 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.777×** | -4.6 | 3e-04 | 27/48 (SW480, A549, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.848× | -4.3 | 0.001 | 17/48 (J82, SW1417, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.824×** | -3.5 | 0.026 | 22/48 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.825×** | -3.5 | 0.026 | 22/48 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.878× | -3.4 | 0.035 | 23/49 (NCI-H2347, A549, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.825×** | -3.4 | 0.035 | 25/47 (SW1417, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.882× | -3.2 | 0.051 | 8/48 (HOP62, A-172, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.845× | -3.1 | 0.080 | 20/48 (NCI-H2347, HT-29, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.845× | -3.1 | 0.080 | 22/48 (A-172, SNU-423, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.842× | -3.0 | 0.093 | 19/49 (KATO III, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8605. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 203 | 10 (2 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.13× (z +19.4) | [[Dinaciclib (drug)]] 5 µM 0.286× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.485× (z -8.5) |
| [[SW1417 (line)]] | alt | 233 | 6 (2 ⚠) | 7 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.447× (z -11.2) |
| [[SW480 (line)]] | alt | 198 | 6 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.34× (z +23.1) | [[Panobinostat (drug)]] 5 µM 0.356× (z -16.3) |
| [[A549 (line)]] | wt | 260 | 4 (1 ⚠) | 7 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.384× (z -14.1) |
| [[BT-474 (line)]] | alt | 141 | 4 (1 ⚠) | 5 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.68× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +11.4) | [[Panobinostat (drug)]] 0.5 µM 0.352× (z -12.9) |
| [[HOP62 (line)]] | alt | 183 | 4 (1 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.320× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.450× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 238 | 5 (2 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.13× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -23.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.400× (z -11.9) |
| [[NCI-H2347 (line)]] | alt | 149 | 4 (1 ⚠) | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.218× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.451× (z -9.5) |
| [[PANC-1 (line)]] | alt | 200 | 4 (1 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.34× (z +22.2) | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.512× (z -10.2) |
| [[SNU-423 (line)]] | alt | 158 | 4 (1 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.291× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.481× (z -9.3) |
| [[SW 900 (line)]] | alt | 135 | 8 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.79× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -9.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 190 | 4 (1 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.31× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.239× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.448× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 96.0 | 7 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.459× (z -8.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 231 | 3 (2 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.305× (z -13.0) |
| [[J82 (line)]] | alt | 137 | 1 | 7 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.417× (z -10.2) |
| [[LoVo (line)]] | wt | 132 | 5 (2 ⚠) | 3 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.49× (z +11.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -17.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 316 | 2 (1 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.409× (z -11.5) |
| [[H4 (line)]] | wt | 110 | 6 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 5.32× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.19× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -11.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 114 | 5 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.50× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.399× (z -9.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 125 | 6 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.98× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.386× (z -11.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 171 | 3 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -14.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 177 | 3 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.384× (z -11.0) |
| [[C32 (line)]] | wt | 148 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -12.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 143 | 2 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +9.9) | [[Lonafarnib (drug)]] 5 µM 0.0430× (z -17.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.424× (z -9.3) |
| [[LS 180 (line)]] | wt | 144 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.467× (z -9.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 133 | 1 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.472× (z -9.3) |
| [[KATO III (line)]] | alt | 112 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.90× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -16.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 297 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.310× (z -12.4) |
| [[NCI-H2030 (line)]] | alt | 217 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -18.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 151 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -14.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 117 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +18.6) | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -10.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 72.1 | 4 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.61× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 160 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -15.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 249 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.420× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 176 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +11.1) | — |
| [[SK-MEL-2 (line)]] | alt | 215 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.421× (z -9.2) |
| [[SNU-1 (line)]] | wt | 216 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -14.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 227 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.85× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -17.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 256 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.364× (z -10.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 110 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 137 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.27× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.394× (z -12.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 280 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -11.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 195 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -10.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 140 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.332× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 301 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0510× (z -16.3) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 171 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.0583× (z -8.6) |
| [[RKO (line)]] | wt | 226 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +9.0) | — |
| [[NCI-H596 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 166 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8605), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF11]] | +0.59 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[MAST2]] | +0.59 | +0.73 / +0.57 | both halves | 1e-05 |  |
| [[CHD7]] | +0.57 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[PCNX1]] | +0.57 | +0.65 / +0.39 | both halves | 5e-05 |  |
| [[SFMBT1]] | +0.57 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[B3GALNT2]] | +0.54 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[SRPK2]] | +0.54 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[FAM135A]] | +0.54 | +0.62 / +0.40 | both halves | 4e-05 |  |
| [[SPECC1L]] | +0.54 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[BMPR1A]] | +0.54 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[LRFN4]] | +0.53 | +0.49 / +0.36 | both halves | 1e-04 |  |
| [[NRF1]] | +0.53 | +0.57 / +0.43 | both halves | 4e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE4A]] | -0.62 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[RTF2]] | -0.60 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[ZNF17]] | -0.59 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[LTN1]] | -0.58 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[TMCO1]] | -0.57 | -0.66 / -0.41 | both halves | 4e-05 |  |
| [[TOX4]] | -0.57 | -0.68 / -0.48 | both halves | 2e-05 |  |
| [[ZNF548]] | -0.56 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[SRP68]] | -0.55 | -0.74 / -0.33 | both halves | 1e-04 |  |
| [[SF3B1]] | -0.55 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[RLIM]] | -0.53 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[GOLGB1]] | -0.52 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[DBT]] | -0.52 | -0.59 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises MEMO1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SOBP]] | B | SOBP activity raises MEMO1's level | lines that do not express SOBP (19) vs lines expressing it (31) | 1.38× lower at baseline in the lines without SOBP | 0.090 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[PALS2]] | C | PALS2 activity raises MEMO1's level | lines that do not express PALS2 (3) vs lines expressing it (47) | 1.67× lower at baseline in the lines without PALS2 | 0.099 | ⚠ few lines (3 vs 47); across organs; also absent: TMCC2, SACS, ANKRD44; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 210]] — tRNA processing; 13 genes; every member is in the + arm (projection on the module's main direction -0.639). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.1, -14.5); signed map (8.3, -3.1). **Vector** length 100, 39.0% of its response variance represented; |z| ≥ 3 in 1,244 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | +2.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.7 | +8.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.2 | +8.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +15.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.9 | +2.5 |
|  | [[EX229 (drug)]] 5 µM |  | +3.4 | +3.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.6 | +2.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +0.5 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -9.6 | -0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.9 | +4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.2 | -11.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -0.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.2 | -10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -3.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.9 | +0.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.2 | -2.8 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | mediator of cell motility 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.3 — chr2:31,865,060-32,011,230 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-27, MEMO; previously C2orf4 |
| Reactome | 3 pathways, smallest: ERBB2 Regulates Cell Motility; Signaling by ERBB2; Signaling by Receptor Tyrosine Kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y316](https://www.uniprot.org/uniprotkb/Q9Y316) (Protein MEMO1):

> May control cell migration by relaying extracellular chemotactic signals to the microtubule cytoskeleton. Mediator of ERBB2 signaling. The MEMO1-RHOA-DIAPH1 signaling pathway plays an important role in ERBB2-dependent stabilization of microtubules at the cell cortex. It controls the localization of APC and CLASP2 to the cell membrane, via the regulation of GSK3B activity. In turn, membrane-bound APC allows the localization of the MACF1 to the cell membrane, which is required for microtubule …

**Summary**, from NCBI Gene [51072](https://www.ncbi.nlm.nih.gov/gene/51072):

> Involved in regulation of microtubule-based process. Located in cytosol and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14014](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14014) · Entrez [51072](https://www.ncbi.nlm.nih.gov/gene/51072) · UniProt [Q9Y316](https://www.uniprot.org/uniprotkb/Q9Y316) · Ensembl [ENSG00000162959](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162959)

## Data

Gene col 8605: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8605); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8605, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8605]; `tensor/DDL_lfc|DDL_z.npy` [8605]; `embed/gene_vectors.npy` [8605]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8605 or target_col == 8605). Every well: [[MEMO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MEMO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
