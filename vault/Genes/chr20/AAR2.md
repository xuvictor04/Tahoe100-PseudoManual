---
symbol: "AAR2"
type: "gene"
col: 5162
ensembl_id: "ENSG00000131043"
name: "AAR2 splicing factor"
location: "20q11.23"
module: 119
arm: "+"
pooled_cpm: 25.43
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# AAR2

*AAR2 splicing factor* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.44× (z +18.0, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.403× (z -20.1, q 0e+00, down in 31 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.622× (z -15.5, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KTI12]] (+0.74, fdr 7e-06), [[METTL16]] (+0.72, fdr 7e-06), [[TRMT10C]] (+0.66, fdr 7e-06); moves opposite to [[CAMTA1]] (-0.54, fdr 1e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5162.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.44×** | +18.0 | 0e+00 | 47/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.49×** | +11.0 | 9e-26 | 35/47 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +10.7 | 3e-24 | 33/46 (CFPAC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +9.6 | 1e-19 | 35/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +7.8 | 4e-13 | 34/48 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +7.8 | 4e-13 | 28/48 (PANC-1, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +6.9 | 5e-10 | 31/48 (SK-MEL-2, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +6.1 | 7e-08 | 22/47 (HS-578T, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +5.8 | 6e-07 | 17/47 (NCI-H1792, NCI-H1573, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.22×** | +4.6 | 2e-04 | 20/48 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.46×** | +4.5 | 3e-04 | 11/48 (MIA PaCa-2, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.20×** | +4.2 | 0.001 | 17/47 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +4.2 | 0.001 | 15/47 (LOX-IMVI, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.19× | +4.1 | 0.002 | 14/48 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.17× | +3.7 | 0.008 | 13/48 (NCI-H2347, NCI-H2030, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.14× | +3.0 | 0.076 | 11/48 (PANC-1, SW480, …) | top dose only |  |
| [[Gemfibrozil (drug)]] 0.05 µM |  | 1.14× | +3.0 | 0.076 | 4/48 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5162.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.403×** | -20.1 | 0e+00 | 31/33 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.459×** | -18.0 | 0e+00 | 33/44 (Panc 03.27, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.622×** | -15.5 | 0e+00 | 43/47 (SW1417, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.550×** | -13.3 | 6e-38 | 33/48 (RKO, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.594×** | -11.5 | 1e-28 | 33/47 (RKO, HS-578T, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.755×** | -9.2 | 5e-18 | 32/48 (SW1417, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.671×** | -8.8 | 7e-17 | 27/46 (J82, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.719×** | -7.0 | 1e-10 | 20/38 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.754×** | -6.5 | 5e-09 | 26/48 (SW1417, LoVo, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.761×** | -6.3 | 2e-08 | 20/48 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.944× | -4.7 | 1e-04 | 3/48 (SW 1271, SW48, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.821×** | -4.5 | 3e-04 | 18/48 (SW1417, A498, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.843× | -3.8 | 0.007 | 16/48 (NCI-H2030, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.851× | -3.7 | 0.008 | 12/48 (SW1417, KATO III, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.867× | -3.3 | 0.039 | 13/48 (BT-474, A498, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5162. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 49.2 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.39× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -13.6) |
| [[NCI-H2030 (line)]] | alt | 32.7 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.29× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.160× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 25.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 21.1 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 18.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -10.2) |
| [[SW480 (line)]] | alt | 28.2 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.66× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.0676× (z -30.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 23.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -8.9) |
| [[AN3 CA (line)]] | alt | 25.6 | 0 | 2 | — | [[Ponatinib (drug)]] 5 µM 0.0811× (z -9.8) |
| [[BT-474 (line)]] | alt | 21.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.346× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 24.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.73× (z +8.5) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.309× (z -9.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 21.8 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -10.0) |
| [[J82 (line)]] | alt | 27.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -17.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 39.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -10.6) |
| [[RKO (line)]] | wt | 31.0 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -13.8) |
| [[SHP-77 (line)]] | alt | 19.9 | 0 | 2 (1 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.199× (z -9.5) |
| [[A-172 (line)]] | wt | 20.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -16.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 24.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -11.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 21.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -12.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 25.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -8.6) |
| [[COLO 205 (line)]] | alt | 30.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -10.3) |
| [[H4 (line)]] | wt | 20.6 | 0 | 1 | — | [[Thymol (drug)]] 0.05 µM 0.0570× (z -13.4) |
| [[HepG2_C3A (line)]] | wt | 31.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -13.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 19.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -10.3) |
| [[hTERT-HPNE (line)]] | wt | 14.8 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0957× (z -12.1) |
| [[KATO III (line)]] | alt | 39.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 37.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[PANC-1 (line)]] | alt | 18.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -13.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 33.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -11.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 18.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -9.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5162), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KTI12]] | +0.74 | +0.61 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[METTL16]] | +0.72 | +0.72 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[TRMT10C]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[E2F6]] | +0.65 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[CCDC12]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[TRMT44]] | +0.65 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[MCRS1]] | +0.64 | +0.55 / +0.68 | both halves | 1e-05 | STRING 460 |
| [[MRPL27]] | +0.64 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[SNRPE]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 | STRING 775 |
| [[LLPH]] | +0.63 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[POLR3A]] | +0.63 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[YRDC]] | +0.63 | +0.57 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMTA1]] | -0.54 | -0.54 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises AAR2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.705). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.4, -9.0); signed map (-14.0, -21.0). **Vector** length 88.6, 18.4% of its response variance represented; |z| ≥ 3 in 980 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.7 | +10.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +7.1 | +7.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.8 | +18.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.8 | +11.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.4 | +2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.4 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +7.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | -0.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.7 | +2.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.2 | -8.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -13.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -11.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.5 | -18.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -15.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -9.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.5 | -2.1 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.7 | -1.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | AAR2 splicing factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:36,236,131-36,270,918 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA234K24.2; previously C20orf4 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y312](https://www.uniprot.org/uniprotkb/Q9Y312) (Protein AAR2 homolog):

> Component of the U5 snRNP complex that is required for spliceosome assembly and for pre-mRNA splicing.

**Summary**, from NCBI Gene [25980](https://www.ncbi.nlm.nih.gov/gene/25980):

> This gene encodes the homolog of the yeast A1-alpha2 repressin protein that is involved in mRNA splicing. Alternately spliced transcript variants have been found for this gene. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:15886](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15886) · Entrez [25980](https://www.ncbi.nlm.nih.gov/gene/25980) · UniProt [Q9Y312](https://www.uniprot.org/uniprotkb/Q9Y312) · Ensembl [ENSG00000131043](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131043)

## Data

Gene col 5162: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5162); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5162, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5162]; `tensor/DDL_lfc|DDL_z.npy` [5162]; `embed/gene_vectors.npy` [5162]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5162 or target_col == 5162). Every well: [[AAR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AAR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
