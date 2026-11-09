---
symbol: "UBXN2B"
type: "gene"
col: 13246
ensembl_id: "ENSG00000215114"
name: "UBX domain protein 2B"
location: "8q12.1"
module: 17
arm: "+"
pooled_cpm: 39.21
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# UBXN2B

*UBX domain protein 2B* — 8q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.51× (z +7.2, q 3e-10, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.475× (z -18.3, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS31P4]] (+0.72, fdr 1e-05), [[THOC1]] (+0.68, fdr 7e-06), [[MRPS31P5-1]] (+0.67, fdr 7e-06); moves opposite to [[SFXN5]] (-0.59, fdr 1e-05), [[LINC02798]] (-0.58, fdr 1e-05), [[GARIN1A]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13246.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +7.2 | 3e-10 | 30/48 (LS 180, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.08×** | +6.7 | 6e-09 | 33/49 (SW480, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +6.6 | 1e-08 | 32/48 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.24×** | +5.4 | 8e-06 | 25/48 (NCI-H2030, J82, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.25×** | +5.4 | 8e-06 | 24/48 (Panc 03.27, HOP62, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +5.2 | 2e-05 | 26/48 (A498, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +4.3 | 0.001 | 20/48 (LS 180, A498, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.57×** | +4.1 | 0.002 | 18/48 (NCI-H2030, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.9 | 0.005 | 23/47 (HT-29, A-427, …) | rises with dose | composition shift |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.17× | +3.9 | 0.006 | 8/48 (RKO, COLO 205, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.24×** | +3.8 | 0.007 | 18/48 (RKO, Panc 03.27, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.24×** | +3.7 | 0.009 | 15/48 (hTERT-HPNE, BT-474, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +3.6 | 0.014 | 15/48 (CHP-212, AsPC-1, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +3.5 | 0.019 | 12/48 (SW48, HOP62, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.5 | 0.019 | 19/48 (NCI-H2347, hTERT-HPNE, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.019 | 19/47 (KATO III, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.024 | 16/48 (KATO III, HT-29, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.056 | 8/48 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13246.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.475×** | -18.3 | 0e+00 | 46/48 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.690×** | -6.5 | 2e-08 | 26/47 (Panc 03.27, SHP-77, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.692×** | -6.4 | 2e-08 | 32/48 (HEC-1-A, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.694×** | -6.1 | 1e-07 | 30/48 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.792×** | -5.8 | 8e-07 | 26/48 (BT-474, Hs 766T, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.710×** | -5.8 | 8e-07 | 25/47 (SNU-423, NCI-H460, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.744×** | -4.8 | 1e-04 | 25/44 (HCT15, A-427, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.758×** | -4.7 | 2e-04 | 22/41 (SW480, KATO III, …) | all doses, flat | composition shift |
| [[Thymol (drug)]] 5 µM |  | 0.845× | -4.2 | 0.002 | 17/48 (HS-578T, LS 180, …) | rises with dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.808×** | -3.7 | 0.010 | 17/48 (HS-578T, RPMI-7951, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.667×** | -3.7 | 0.011 | 18/42 (RPMI-7951, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.811×** | -3.5 | 0.020 | 19/47 (MIA PaCa-2, SHP-77, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.828×** | -3.3 | 0.041 | 18/48 (PANC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.836× | -3.1 | 0.068 | 10/48 (HS-578T, NCI-H1573, …) | inconsistent across doses |  |
| [[Ritonavir (drug)]] 5 µM |  | 0.882× | -3.1 | 0.071 | 11/48 (J82, A498, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.831×** | -3.0 | 0.095 | 10/48 (AN3 CA, MIA PaCa-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13246. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 34.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0960× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 43.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 40.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -13.5) |
| [[SW480 (line)]] | alt | 45.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0412× (z -32.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -9.8) |
| [[A-172 (line)]] | wt | 26.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -8.9) |
| [[A-427 (line)]] | wt | 48.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.183× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A498 (line)]] | wt | 37.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -9.9) |
| [[A549 (line)]] | wt | 54.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -13.9) |
| [[AN3 CA (line)]] | alt | 34.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.115× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 40.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -11.3) |
| [[C-33 A (line)]] | alt | 60.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[C32 (line)]] | wt | 38.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 44.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -10.4) |
| [[HCT15 (line)]] | alt | 52.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0841× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HepG2_C3A (line)]] | wt | 28.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -10.0) |
| [[HOP62 (line)]] | alt | 31.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -9.7) |
| [[Hs 766T (line)]] | wt | 17.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -11.0) |
| [[HS-578T (line)]] | alt | 44.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HT-29 (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.218× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[LoVo (line)]] | wt | 21.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 49.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 42.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -12.8) |
| [[NCI-H460 (line)]] | wt | 28.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -13.7) |
| [[NCI-H661 (line)]] | alt | 53.2 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0800× (z -9.4) |
| [[PANC-1 (line)]] | alt | 54.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -11.0) |
| [[RKO (line)]] | wt | 52.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 30.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0997× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[SHP-77 (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SW 1271 (line)]] | alt | 56.5 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0841× (z -8.5) |
| [[SW 900 (line)]] | alt | 42.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -13.1) |
| [[SW1417 (line)]] | alt | 21.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13246), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS31P4]] | +0.72 | +0.51 / +0.75 | both halves | 1e-05 |  |
| [[THOC1]] | +0.68 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[MRPS31P5-1]] | +0.67 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[COMMD2]] | +0.66 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[HEATR6]] | +0.66 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[TRAPPC11]] | +0.65 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[FIG4]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[PEX2]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[WDR11]] | +0.64 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[ESD]] | +0.63 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ZNF112]] | +0.63 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[USP30]] | +0.62 | +0.64 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFXN5]] | -0.59 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[LINC02798]] | -0.58 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[GARIN1A]] | -0.57 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[TRPV1]] | -0.57 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[COL27A1]] | -0.56 | -0.29 / -0.65 | both halves | 2e-04 |  |
| [[PIPOX]] | -0.56 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[C9]] | -0.55 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[DDX5]] | -0.55 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[LINC00393]] | -0.55 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[STARD4-AS1]] | -0.54 | -0.30 / -0.55 | both halves | 2e-04 |  |
| [[NEK10]] | -0.54 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[SIAH2-AS1]] | -0.54 | -0.35 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises UBXN2B's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF559]] | B | ZNF559 activity raises UBXN2B's level | lines that do not express ZNF559 (6) vs lines expressing it (44) | 1.56× lower at baseline in the lines without ZNF559 | 0.090 | ⚠ within organs, on part of the lines; also absent: ZNF559-ZNF177, ZNF177, GUCY1A2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.778). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-26.4, -2.6); signed map (-22.6, -14.3). **Vector** length 103, 25.8% of its response variance represented; |z| ≥ 3 in 912 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +5.4 | +4.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.5 | +5.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.1 | +7.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.8 | +5.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.7 | +3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.6 | +3.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.7 | +2.7 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.5 | +1.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.7 | -18.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -5.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.4 | -5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -6.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.1 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | UBX domain protein 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q12.1 — chr8:58,411,359-58,451,501 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p37 |
| Gene groups (HGNC) | UBX domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14CS0](https://www.uniprot.org/uniprotkb/Q14CS0) (UBX domain-containing protein 2B):

> Adapter protein required for Golgi and endoplasmic reticulum biogenesis. Involved in Golgi and endoplasmic reticulum maintenance during interphase and in their reassembly at the end of mitosis. The complex formed with VCP has membrane fusion activity; membrane fusion activity requires USO1-GOLGA2 tethering and BET1L. VCPIP1 is also required, but not its deubiquitinating activity. Together with NSFL1C/p47, regulates the centrosomal levels of kinase AURKA/Aurora A during mitotic progression by …

**Summary**, from NCBI Gene [137886](https://www.ncbi.nlm.nih.gov/gene/137886):

> Predicted to enable ubiquitin binding activity. Involved in several processes, including negative regulation of protein localization to centrosome; positive regulation of mitotic centrosome separation; and protein unfolding. Predicted to be located in Golgi apparatus; endoplasmic reticulum; and spindle pole centrosome. Predicted to be active in cytosol and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27035](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27035) · Entrez [137886](https://www.ncbi.nlm.nih.gov/gene/137886) · UniProt [Q14CS0](https://www.uniprot.org/uniprotkb/Q14CS0) · Ensembl [ENSG00000215114](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215114)

## Data

Gene col 13246: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13246); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13246, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13246]; `tensor/DDL_lfc|DDL_z.npy` [13246]; `embed/gene_vectors.npy` [13246]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13246 or target_col == 13246). Every well: [[UBXN2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBXN2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
