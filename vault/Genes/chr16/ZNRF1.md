---
symbol: "ZNRF1"
type: "gene"
col: 11789
ensembl_id: "ENSG00000186187"
name: "zinc and ring finger 1"
location: "16q23.1"
module: 154
arm: "+"
pooled_cpm: 88.37
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 37
n_dd_up_clean: 0
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# ZNRF1

*zinc and ring finger 1* — 16q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.24× (z +4.4, q 0.007, up in 23 of 47 measured lines) ⚠ cell-cycle shift, explains ~19% of this change.
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.367× (z -21.3, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBA6]] (+0.66, fdr 3e-05), [[CIB1]] (+0.66, fdr 1e-05), [[ATG16L2]] (+0.62, fdr 1e-05); moves opposite to [[ZRANB2-DT]] (-0.62, fdr 3e-05), [[ZMYND11]] (-0.58, fdr 8e-05), [[SLC38A4-AS1]] (-0.58, fdr 3e-05).
> It is in [[Module 154]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[BICDL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11789.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.24×** | +4.4 | 0.007 | 23/47 (RKO, C32, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.19× | +3.8 | 0.044 | 20/47 (RKO, SW48, …) | rises with dose | low cells (technical?) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.19× | +3.6 | 0.067 | 12/48 (HT-29, RKO, …) | inconsistent across doses |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 1.19× | +3.5 | 0.071 | 11/48 (CFPAC-1, NCI-H2347, …) | rises with dose | plate-row cell shift |
| [[PF-06260933 (drug)]] 5 µM |  | 1.33× | +3.1 | 0.19 | 15/48 (SW480, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pimitespib (drug)]] 0.05 µM |  | 1.16× | +3.1 | 0.20 | 11/48 (PANC-1, HS-578T, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 60 in all, 23 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11789.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.367×** | -21.3 | 0e+00 | 42/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.548×** | -18.0 | 0e+00 | 36/48 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.433×** | -16.9 | 0e+00 | 34/43 (NCI-H1792, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.466×** | -16.2 | 0e+00 | 40/49 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.470×** | -14.8 | 0e+00 | 37/45 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.525×** | -13.6 | 2e-40 | 42/48 (SK-MEL-2, SW 900, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.555×** | -12.5 | 9e-34 | 38/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.559×** | -12.3 | 4e-33 | 40/48 (NCI-H1573, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.586×** | -11.3 | 5e-28 | 41/48 (SW 900, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.575×** | -11.2 | 4e-27 | 36/47 (NCI-H1792, SW 900, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.586×** | -10.8 | 2e-25 | 33/48 (LOX-IMVI, SNU-423, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -10.6 | 2e-24 | 29/49 (NCI-H1792, SW 900, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.597×** | -10.4 | 1e-23 | 36/50 (SW 900, SNU-423, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.616×** | -9.8 | 6e-21 | 31/48 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.726×** | -9.6 | 4e-20 | 33/48 (A-172, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.758×** | -8.3 | 4e-15 | 29/48 (J82, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.582×** | -6.0 | 6e-08 | 26/49 (NCI-H460, NCI-H1792, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.772×** | -5.5 | 1e-06 | 24/48 (SW 900, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.735×** | -4.6 | 8e-05 | 25/47 (J82, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.803×** | -4.4 | 3e-04 | 22/48 (CFPAC-1, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.813×** | -4.4 | 3e-04 | 21/48 (HOP62, H4, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.817×** | -4.3 | 4e-04 | 24/48 (MIA PaCa-2, SW48, …) | all doses, stronger at high dose | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.822×** | -4.1 | 7e-04 | 21/47 (SNU-423, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11789. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 194 | 0 | 19 (12 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0961× (z -22.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -18.9) |
| [[NCI-H1792 (line)]] | alt | 319 | 0 | 16 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0997× (z -38.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -20.7) |
| [[HOP62 (line)]] | alt | 163 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -22.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.206× (z -16.8) |
| [[SK-MEL-2 (line)]] | alt | 129 | 0 | 13 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.211× (z -15.3) |
| [[hTERT-HPNE (line)]] | wt | 122 | 0 | 12 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0840× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 57.3 | 0 | 12 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.276× (z -15.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.400× (z -10.7) |
| [[SNU-423 (line)]] | alt | 139 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -15.6) |
| [[LOX-IMVI (line)]] | wt | 64.1 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.206× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -14.6) |
| [[CFPAC-1 (line)]] | alt | 138 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -25.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -17.7) |
| [[NCI-H1573 (line)]] | alt | 85.2 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -19.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -18.9) |
| [[A549 (line)]] | wt | 99.1 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.107× (z -22.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.377× (z -10.5) |
| [[LS 180 (line)]] | wt | 63.7 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -15.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.304× (z -12.8) |
| [[NCI-H2030 (line)]] | alt | 160 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -18.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -14.1) |
| [[J82 (line)]] | alt | 97.1 | 0 | 7 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.366× (z -14.8) |
| [[SHP-77 (line)]] | alt | 144 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.370× (z -9.6) |
| [[HS-578T (line)]] | alt | 95.9 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -16.2) |
| [[RKO (line)]] | wt | 75.2 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.230× (z -13.3) |
| [[A-172 (line)]] | wt | 118 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.377× (z -10.7) |
| [[Hs 766T (line)]] | wt | 93.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.363× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 54.9 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.199× (z -14.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.351× (z -9.9) |
| [[A-427 (line)]] | wt | 84.6 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -22.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.305× (z -13.5) |
| [[SW480 (line)]] | alt | 94.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -21.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 95.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.329× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.460× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 46.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -14.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.208× (z -12.6) |
| [[NCI-H2347 (line)]] | alt | 54.6 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -13.3) |
| [[RPMI-7951 (line)]] | alt | 57.4 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.224× (z -10.9) ⚠ toxic |
| [[C-33 A (line)]] | alt | 86.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 78.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -13.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[Panc 03.27 (line)]] | alt | 36.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.236× (z -12.7) |
| [[SW 1088 (line)]] | alt | 110 | 0 | 2 | — | [[Silodosin (drug)]] 0.05 µM 0.0917× (z -9.1) |
| [[SW48 (line)]] | wt | 60.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -10.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.246× (z -9.3) |
| [[BT-474 (line)]] | alt | 74.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -13.6) |
| [[C32 (line)]] | wt | 33.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.277× (z -9.3) |
| [[H4 (line)]] | wt | 93.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.269× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 43.0 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -9.2) |
| [[LoVo (line)]] | wt | 56.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.500× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -13.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[PANC-1 (line)]] | alt | 71.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.495× (z -8.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 78.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.298× (z -9.1) |
| [[AN3 CA (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 95.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 92.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11789), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBA6]] | +0.66 | +0.73 / +0.45 | both halves | 3e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[CIB1]] | +0.66 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[ATG16L2]] | +0.62 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[CARD19]] | +0.62 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[ETHE1]] | +0.62 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[EPN2]] | +0.61 | +0.63 / +0.46 | both halves | 2e-05 |  |
| [[SEMA4B]] | +0.61 | +0.71 / +0.44 | both halves | 3e-05 |  |
| [[NGLY1]] | +0.61 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[MYO9B]] | +0.60 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[NDRG1]] | +0.59 | +0.67 / +0.44 | both halves | 3e-05 |  |
| [[AHDC1]] | +0.59 | +0.66 / +0.35 | both halves | 1e-04 |  |
| [[ANKRD37]] | +0.59 | +0.62 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZRANB2-DT]] | -0.62 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[ZMYND11]] | -0.58 | -0.62 / -0.37 | both halves | 8e-05 |  |
| [[SLC38A4-AS1]] | -0.58 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[ZNF507]] | -0.56 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[CPNE1]] | -0.56 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[DPH6-DT]] | -0.56 | -0.63 / -0.33 | both halves | 1e-04 |  |
| [[DDX6]] | -0.56 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[UFL1-AS1]] | -0.56 | -0.60 / -0.35 | both halves | 1e-04 |  |
| [[SUCLG2-DT]] | -0.55 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[ATP1A1-AS1]] | -0.55 | -0.65 / -0.25 | both halves | 4e-04 |  |
| [[UTP20]] | -0.54 | -0.59 / -0.39 | both halves | 6e-05 |  |
| [[EIF1B-AS1]] | -0.54 | -0.55 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BICDL1]] | B | BICDL1 activity lowers ZNRF1's level | lines that do not express BICDL1 (12) vs lines expressing it (38) | 1.70× higher at baseline in the lines without BICDL1 | 0.019 | ⚠ within organs, on part of the lines; also absent: ABLIM2, KRT18, LINC00857 |
| [[PMP22]] | B | PMP22 activity raises ZNRF1's level | lines that do not express PMP22 (10) vs lines expressing it (40) | 1.57× lower at baseline in the lines without PMP22 | 0.043 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |
| [[TMEM145]] | B | TMEM145 activity raises ZNRF1's level | lines that do not express TMEM145 (11) vs lines expressing it (39) | 1.57× lower at baseline in the lines without TMEM145 | 0.062 | ⚠ within organs, on part of the lines; also absent: GXYLT2, KCNK13, DLX1 |
| [[TOP2A]] | B | TOP2A activity raises ZNRF1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PPP4R4]] | B | PPP4R4 activity raises ZNRF1's level | lines that do not express PPP4R4 (10) vs lines expressing it (40) | 1.81× lower at baseline in the lines without PPP4R4 | 0.092 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, ENSG00000285804, LINC01088 |
| [[ZFYVE28]] | C | ZFYVE28 activity raises ZNRF1's level | lines that do not express ZFYVE28 (4) vs lines expressing it (46) | 1.80× lower at baseline in the lines without ZFYVE28 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.799). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.5, 2.9); signed map (-5.1, 47.1). **Vector** length 110, 33.4% of its response variance represented; |z| ≥ 3 in 1,628 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.6 | +0.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.9 | +1.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.6 | +2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +4.8 | -3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.2 | -5.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.6 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +1.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.7 | +0.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.4 | +1.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.2 | -8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -13.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -21.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.1 | -12.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.0 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -9.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.8 | -1.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.8 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc and ring finger 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.1 — chr16:74,999,024-75,110,994 (+) |
| Ensembl biotype | protein_coding |
| Also known as | nin283, FLJ14846, DKFZp434E229 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8ND25](https://www.uniprot.org/uniprotkb/Q8ND25) (E3 ubiquitin-protein ligase ZNRF1):

> E3 ubiquitin-protein ligase that plays a role in different processes including cell differentiation, receptor recycling or regulation of inflammation. Mediates the ubiquitination of AKT1 and GLUL, thereby playing a role in neuron cells differentiation. Plays a role in the establishment and maintenance of neuronal transmission and plasticity. Regulates Schwann cells differentiation by mediating ubiquitination of GLUL. Promotes neurodegeneration by mediating 'Lys-48'-linked polyubiquitination and …

**Summary**, from NCBI Gene [84937](https://www.ncbi.nlm.nih.gov/gene/84937):

> This gene encodes an E3 ubiquitin-protein ligase that plays a role in neural-cell differentiation. Overexpression of this gene causes neurite-like elongation. The encoded protein contains both a zinc finger and a RING finger motif and is localized in the endosome/lysosome compartment, indicating that it may be involved in ubiquitin-mediated protein modification, and in synaptic vessicle membranes in neurons. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:18452](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18452) · Entrez [84937](https://www.ncbi.nlm.nih.gov/gene/84937) · UniProt [Q8ND25](https://www.uniprot.org/uniprotkb/Q8ND25) · Ensembl [ENSG00000186187](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186187)

## Data

Gene col 11789: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11789); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11789, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11789]; `tensor/DDL_lfc|DDL_z.npy` [11789]; `embed/gene_vectors.npy` [11789]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11789 or target_col == 11789). Every well: [[ZNRF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNRF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
