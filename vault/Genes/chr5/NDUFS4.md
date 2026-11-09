---
symbol: "NDUFS4"
type: "gene"
col: 8914
ensembl_id: "ENSG00000164258"
name: "NADH:ubiquinone oxidoreductase subunit S4"
location: "5q11.2"
module: 220
arm: "+"
pooled_cpm: 85.18
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 14
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/220"]
generated_by: "tahoemap"
---

# NDUFS4

*NADH:ubiquinone oxidoreductase subunit S4* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.32× (z +11.3, q 5e-27, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.413× (z -32.2, q 0e+00, down in 48 of 49 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL22]] (+0.80, fdr 7e-06), [[ABCB7]] (+0.68, fdr 1e-05), [[METTL14]] (+0.67, fdr 7e-06); moves opposite to [[SMG1P6]] (-0.56, fdr 2e-04).
> It is in [[Module 220]], a single-armed module (Respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8914.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.32×** | +11.3 | 5e-27 | 44/49 (NCI-H460, LOX-IMVI, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.38×** | +8.4 | 1e-14 | 30/48 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +5.8 | 1e-06 | 20/48 (LS 180, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[NG25 (drug)]] 5 µM |  | **1.49×** | +5.3 | 1e-05 | 36/47 (C32, SW48, …) | top dose only | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.23×** | +5.3 | 1e-05 | 23/48 (NCI-H1792, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.44×** | +4.9 | 9e-05 | 26/48 (C32, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.22×** | +4.8 | 2e-04 | 22/47 (NCI-H460, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.17× | +4.0 | 0.005 | 17/48 (LOX-IMVI, NCI-H1792, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +4.0 | 0.005 | 18/48 (A-427, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.8 | 0.009 | 15/48 (LOX-IMVI, A-427, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.7 | 0.012 | 21/48 (KATO III, SW 900, …) | rises with dose |  |
| [[Fumaric acid (drug)]] 5 µM |  | 1.13× | +3.1 | 0.082 | 4/49 (CFPAC-1, SW 1088, …) | rises with dose | plate-row cell shift; position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.090 | 9/48 (MIA PaCa-2, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8914.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.413×** | -32.2 | 0e+00 | 48/49 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.559×** | -14.9 | 0e+00 | 45/48 (A-172, SNU-423, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.590×** | -13.1 | 1e-36 | 42/48 (SW480, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.592×** | -13.0 | 2e-36 | 42/50 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.644×** | -11.3 | 1e-27 | 42/48 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.670×** | -10.3 | 6e-23 | 46/48 (CFPAC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.675×** | -10.1 | 5e-22 | 39/48 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.750×** | -7.4 | 1e-11 | 32/48 (CFPAC-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.775×** | -6.3 | 2e-08 | 24/44 (SHP-77, LoVo, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.785×** | -6.2 | 3e-08 | 26/48 (AsPC-1, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.799×** | -5.5 | 2e-06 | 24/47 (CFPAC-1, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.813×** | -5.3 | 5e-06 | 27/48 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.707×** | -4.7 | 1e-04 | 22/49 (NCI-H2347, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.843× | -4.4 | 5e-04 | 20/48 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.892× | -4.2 | 0.001 | 15/48 (NCI-H2347, AN3 CA, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.845× | -4.0 | 0.002 | 16/47 (J82, A-427, …) | inconsistent across doses |  |
| [[OTS514 (drug)]] 5 µM |  | **0.745×** | -4.0 | 0.003 | 22/46 (SHP-77, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.860× | -3.9 | 0.003 | 17/48 (LS 180, SW480, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.902× | -3.8 | 0.005 | 6/48 (SHP-77, H4, …) | top dose only |  |
| [[Berbamine (drug)]] 0.5 µM |  | 0.888× | -3.0 | 0.066 | 6/48 (KATO III, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8914. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 183 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -15.9) |
| [[LOX-IMVI (line)]] | wt | 117 | 2 | 4 | [[TAK-901 (drug)]] 0.05 µM 2.38× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -21.3) |
| [[NCI-H460 (line)]] | wt | 99.4 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 2.61× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -23.9) |
| [[SW480 (line)]] | alt | 72.9 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -27.2) |
| [[CFPAC-1 (line)]] | alt | 115 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -24.7) |
| [[RKO (line)]] | wt | 94.3 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -24.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -23.7) |
| [[SNU-423 (line)]] | alt | 85.3 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -18.4) |
| [[C32 (line)]] | wt | 77.9 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -13.5) |
| [[LoVo (line)]] | wt | 81.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -21.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -17.0) |
| [[AsPC-1 (line)]] | alt | 92.7 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -19.7) |
| [[LS 180 (line)]] | wt | 86.9 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -11.9) |
| [[NCI-H1792 (line)]] | alt | 76.7 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -22.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 98.3 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -20.0) |
| [[SNU-1 (line)]] | wt | 96.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -19.3) |
| [[A-172 (line)]] | wt | 81.5 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.396× (z -12.1) |
| [[HCT15 (line)]] | alt | 87.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -13.9) |
| [[hTERT-HPNE (line)]] | wt | 75.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -15.3) |
| [[J82 (line)]] | alt | 64.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -13.3) |
| [[MIA PaCa-2 (line)]] | alt | 72.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 78.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -17.2) |
| [[NCI-H23 (line)]] | alt | 68.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -9.8) |
| [[PANC-1 (line)]] | alt | 96.6 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -18.3) |
| [[RPMI-7951 (line)]] | alt | 77.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -13.5) |
| [[SHP-77 (line)]] | alt | 89.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0946× (z -27.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -17.1) |
| [[SW 1088 (line)]] | alt | 127 | 0 | 2 | — | [[Irinotecan (hydrochloride) (drug)]] 0.05 µM 0.0773× (z -10.4) |
| [[SW 900 (line)]] | alt | 115 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -13.2) |
| [[SW1417 (line)]] | alt | 54.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -16.8) |
| [[SW48 (line)]] | wt | 72.2 | 1 | 1 | [[TAK-901 (drug)]] 0.05 µM 3.37× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -10.2) |
| [[A-427 (line)]] | wt | 94.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -19.0) |
| [[A498 (line)]] | wt | 68.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -11.1) |
| [[A549 (line)]] | wt | 99.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -18.4) |
| [[AN3 CA (line)]] | alt | 115 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -12.4) |
| [[BT-474 (line)]] | alt | 60.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -9.5) |
| [[C-33 A (line)]] | alt | 65.6 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -9.7) |
| [[CHP-212 (line)]] | wt | 93.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -12.8) |
| [[COLO 205 (line)]] | alt | 92.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -15.4) |
| [[HEC-1-A (line)]] | alt | 84.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -19.5) |
| [[HepG2_C3A (line)]] | wt | 117 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -14.0) |
| [[HOP62 (line)]] | alt | 34.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -13.9) |
| [[Hs 766T (line)]] | wt | 69.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -13.8) |
| [[HS-578T (line)]] | alt | 103 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -13.9) |
| [[HT-29 (line)]] | alt | 73.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -14.8) |
| [[KATO III (line)]] | alt | 61.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 42.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 67.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.433× (z -8.9) |
| [[H4 (line)]] | wt | 88.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 127 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8914), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 6 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL22]] | +0.80 | +0.76 / +0.78 | both halves | 7e-06 | STRING 450 |
| [[ABCB7]] | +0.68 | +0.52 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[METTL14]] | +0.67 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[MNAT1]] | +0.66 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[CWC15]] | +0.66 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[TMEM126A]] | +0.65 | +0.54 / +0.64 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[MRPL1]] | +0.64 | +0.57 / +0.62 | both halves | 9e-06 | STRING 427 |
| [[IRAK1BP1]] | +0.63 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[IFTAP]] | +0.62 | +0.36 / +0.64 | both halves | 9e-05 |  |
| [[FAM133B]] | +0.62 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[ESD]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[PEX2]] | +0.61 | +0.65 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMG1P6]] | -0.56 | -0.32 / -0.58 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NDUFS4's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZDHHC17]] | C | ZDHHC17's natural level strengthens NDUFS4's drug response | ZDHHC17's natural level across 50 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.10; direction clear | 0.037 | ⚠ tissue can mimic it; precision caveat |
| [[CUL5]] | C | CUL5's natural level strengthens NDUFS4's drug response | CUL5's natural level across 50 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.19; direction not clear | 0.053 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[FAM204A]] | C | FAM204A's natural level strengthens NDUFS4's drug response | FAM204A's natural level across 50 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.11; direction not clear | 0.061 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[MTMR3]] | C | MTMR3's natural level strengthens NDUFS4's drug response | MTMR3's natural level across 50 lines (lineage-adjusted; a glimpse) | r +0.60, reverse -0.10; direction not clear | 0.0995 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 220]] — Respiratory electron transport; 11 genes; every member is in the + arm (projection on the module's main direction 0.853). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-23.2, -2.4); signed map (-22.0, -11.7). **Vector** length 106, 29.0% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +10.1 | +5.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.8 | +3.7 |
|  | [[NG25 (drug)]] 5 µM |  | +4.6 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +4.3 | -3.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.3 | +11.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.0 | +1.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | -3.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.5 | -1.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.0 | -14.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -32.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -13.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -13.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.1 | -0.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.4 | -2.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.3 | -1.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.1 | -0.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit S4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q11.2 — chr5:53,560,633-53,683,338 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AQDQ, CI-18 |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O43181](https://www.uniprot.org/uniprotkb/O43181) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone.

**Summary**, from NCBI Gene [4724](https://www.ncbi.nlm.nih.gov/gene/4724):

> This gene encodes an nuclear-encoded accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (complex I, or NADH:ubiquinone oxidoreductase). Complex I removes electrons from NADH and passes them to the electron acceptor ubiquinone. Mutations in this gene can cause mitochondrial complex I deficiencies such as Leigh syndrome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:7711](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7711) · Entrez [4724](https://www.ncbi.nlm.nih.gov/gene/4724) · UniProt [O43181](https://www.uniprot.org/uniprotkb/O43181) · Ensembl [ENSG00000164258](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164258)

## Data

Gene col 8914: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8914); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8914, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8914]; `tensor/DDL_lfc|DDL_z.npy` [8914]; `embed/gene_vectors.npy` [8914]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8914 or target_col == 8914). Every well: [[NDUFS4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFS4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
