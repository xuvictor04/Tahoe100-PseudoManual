---
symbol: "NFXL1"
type: "gene"
col: 9955
ensembl_id: "ENSG00000170448"
name: "nuclear transcription factor, X-box binding like 1"
location: "4p12"
module: 49
arm: "+"
pooled_cpm: 71.31
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 27
n_dd_up_clean: 8
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# NFXL1

*nuclear transcription factor, X-box binding like 1* — 4p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.59× (z +7.7, q 7e-12, up in 41 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.38× (z +5.3, q 3e-05, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.454× (z -13.2, q 8e-37, down in 42 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.703× (z -7.2, q 1e-10, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OSTC]] (+0.76, fdr 7e-06), [[PDIA5]] (+0.73, fdr 7e-06), [[SRPRB]] (+0.72, fdr 7e-06); moves opposite to [[CHMP1B]] (-0.60, fdr 2e-05), [[TRIP12]] (-0.55, fdr 1e-05), [[YWHAZ]] (-0.55, fdr 1e-04).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC2A10]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9955.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.59×** | +7.7 | 7e-12 | 41/48 (A498, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +5.3 | 3e-05 | 27/48 (NCI-H1573, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.79×** | +5.1 | 7e-05 | 36/48 (A498, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.62×** | +4.2 | 0.004 | 25/48 (SW480, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.021 | 23/48 (LoVo, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.51×** | +3.6 | 0.024 | 19/48 (NCI-H1792, A498, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.26×** | +3.6 | 0.024 | 20/48 (Hs 766T, SHP-77, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.036 | 20/48 (A498, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.057 | 14/47 (SW480, AN3 CA, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 12 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9955.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.454×** | -13.2 | 8e-37 | 42/49 (C-33 A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.443×** | -13.0 | 2e-36 | 37/44 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.596×** | -8.0 | 3e-13 | 29/45 (RPMI-7951, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.703×** | -7.2 | 1e-10 | 38/48 (HS-578T, A498, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.716×** | -5.6 | 3e-06 | 32/48 (SW480, SW48, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.731×** | -5.0 | 5e-05 | 29/48 (A-172, A498, …) | inconsistent across doses | composition shift |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.737×** | -4.9 | 7e-05 | 32/49 (RKO, HEC-1-A, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.749×** | -4.8 | 1e-04 | 29/48 (SW480, SW48, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.776×** | -4.7 | 1e-04 | 26/49 (RPMI-7951, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.751×** | -4.6 | 2e-04 | 32/48 (HT-29, COLO 205, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **0.766×** | -4.3 | 8e-04 | 25/48 (KATO III, CHP-212, …) | inconsistent across doses | low cells (technical?) |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.778×** | -4.1 | 0.002 | 28/49 (NCI-H1573, SW 900, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.796×** | -3.8 | 0.006 | 27/48 (KATO III, HCT15, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.797×** | -3.8 | 0.006 | 24/48 (SW480, SW48, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.792×** | -3.8 | 0.006 | 24/48 (HT-29, NCI-H1573, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.793×** | -3.8 | 0.006 | 24/49 (HT-29, RKO, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.797×** | -3.7 | 0.007 | 25/48 (SW 1088, HT-29, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.800×** | -3.6 | 0.009 | 26/49 (HT-29, COLO 205, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.802×** | -3.6 | 0.010 | 21/49 (COLO 205, HT-29, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.668×** | -3.5 | 0.012 | 24/49 (HOP62, SW 900, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | **0.820×** | -3.4 | 0.018 | 16/48 (NCI-H2030, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.818×** | -3.4 | 0.020 | 19/48 (COLO 205, SW48, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 0.05 µM |  | **0.813×** | -3.2 | 0.027 | 18/48 (HS-578T, COLO 205, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.819×** | -3.2 | 0.031 | 19/48 (RKO, NCI-H1573, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.827×** | -3.2 | 0.035 | 16/48 (NCI-H23, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9955. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 97.3 | 4 (3 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.93× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.357× (z -13.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 77.1 | 1 (1 ⚠) | 5 (4 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.14× (z +9.3) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 0.05 µM 0.308× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.587× (z -8.6) |
| [[A-172 (line)]] | wt | 40.7 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -17.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 90.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -16.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 66.8 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.29× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -12.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 80.2 | 0 | 4 (1 ⚠) | — | [[Acetohexamide (drug)]] 0.5 µM 0.0679× (z -11.1) |
| [[HOP62 (line)]] | alt | 74.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.317× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 101 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.92× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -10.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 91.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -15.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 213 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -11.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 45.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -12.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 84.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -10.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 68.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.50× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.295× (z -11.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 104 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0985× (z -13.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 130 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -13.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 78.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -14.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 81.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.375× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 100 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.317× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 37.7 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.57× (z +8.7) ⚠ unreliable plate only | — |
| [[C-33 A (line)]] | alt | 73.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0626× (z -23.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 86.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -11.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 71.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -8.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 71.5 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.480× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 71.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 66.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 49.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -9.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -13.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 56.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 59.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 66.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 86.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 93.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 58.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9955), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OSTC]] | +0.76 | +0.78 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[PDIA5]] | +0.73 | +0.66 / +0.77 | both halves | 7e-06 |  |
| [[SRPRB]] | +0.72 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[DNAJC25]] | +0.71 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[SLC33A1]] | +0.69 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[COG3]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[RINT1]] | +0.68 | +0.63 / +0.67 | both halves | 7e-06 | STRING 615 |
| [[COG6]] | +0.66 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[TXNDC11]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.65 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[TGDS]] | +0.65 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[SSR2]] | +0.65 | +0.58 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHMP1B]] | -0.60 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[TRIP12]] | -0.55 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[YWHAZ]] | -0.55 | -0.34 / -0.59 | both halves | 1e-04 |  |
| [[PURB]] | -0.54 | -0.53 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC2A10]] | B | SLC2A10 activity raises NFXL1's level | lines that do not express SLC2A10 (18) vs lines expressing it (32) | 1.22× lower at baseline in the lines without SLC2A10 | 0.009 | ⚠ within organs, on part of the lines; also absent: SARDH, CSF1 |
| [[CADPS2]] | B | CADPS2 activity raises NFXL1's level | lines that do not express CADPS2 (14) vs lines expressing it (36) | 1.30× lower at baseline in the lines without CADPS2 | 0.055 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.766). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.3, -34.3); signed map (-53.1, 10.7). **Vector** length 117, 34.4% of its response variance represented; |z| ≥ 3 in 1,018 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *XBP1(S) activates chaperone genes* (reactome, mean cos +0.55 to 8); *IRE1alpha activates chaperones* (reactome, mean cos +0.55 to 8); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.55 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.4 | +7.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.8 | +3.5 |
|  | [[EX229 (drug)]] 5 µM |  | +4.6 | +5.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.6 | +4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.3 | +3.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +4.0 | +3.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.2 | -3.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.4 | -5.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.2 | -4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -7.2 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -3.0 | -3.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | nuclear transcription factor, X-box binding like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p12 — chr4:47,847,233-47,914,667 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HOZFP |
| Gene groups (HGNC) | Ring finger proteins; Zinc fingers NFX1-type; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

UniProt [Q6ZNB6](https://www.uniprot.org/uniprotkb/Q6ZNB6) carries no function annotation.

**Summary**, from NCBI Gene [152518](https://www.ncbi.nlm.nih.gov/gene/152518):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II transcription regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of DNA-templated transcription. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18726](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18726) · Entrez [152518](https://www.ncbi.nlm.nih.gov/gene/152518) · UniProt [Q6ZNB6](https://www.uniprot.org/uniprotkb/Q6ZNB6) · Ensembl [ENSG00000170448](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170448)

## Data

Gene col 9955: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9955); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9955, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9955]; `tensor/DDL_lfc|DDL_z.npy` [9955]; `embed/gene_vectors.npy` [9955]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9955 or target_col == 9955). Every well: [[NFXL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFXL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
