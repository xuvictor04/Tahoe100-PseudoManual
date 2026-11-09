---
symbol: "ZNF213-AS1"
type: "gene"
col: 15405
ensembl_id: "ENSG00000263072"
name: "ZNF213 antisense RNA 1"
location: "16p13.3"
module: 15
arm: "+"
pooled_cpm: 8.59
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 7
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ZNF213-AS1

*ZNF213 antisense RNA 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.86× (z +33.7, q 0e+00, up in 43 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.600× (z -6.3, q 1e-07, down in 25 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.696× (z -4.5, q 7e-04, down in 21 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (LoVo 0.137×, KATO III 0.150×, C-33 A 0.107×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Nafamostat (mesylate) (drug)]] 0.05 µM in 1 line (RKO 0.0475×); [[Harringtonine (drug)]] 0.05 µM in 1 line (A549 0.0666×); [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (SHP-77 0.0861×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF3C2-AS2]] (+0.80, fdr 7e-06), [[MSTO1]] (+0.80, fdr 7e-06), [[ZNF596]] (+0.79, fdr 7e-06); moves opposite to [[THEM6]] (-0.66, fdr 2e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15405.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.86×** | +33.7 | 0e+00 | 43/43 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.05×** | +16.7 | 0e+00 | 39/44 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.01×** | +13.1 | 5e-37 | 36/44 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.62×** | +8.4 | 6e-15 | 26/48 (BT-474, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.05×** | +8.2 | 3e-14 | 16/25 (SW1417, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +7.0 | 3e-10 | 24/38 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.53×** | +5.2 | 1e-05 | 21/48 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +5.1 | 2e-05 | 6/15 (SW1417, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.47×** | +4.8 | 1e-04 | 14/47 (SW480, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.003 | 17/45 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.25×** | +3.9 | 0.006 | 20/48 (A498, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.36×** | +3.8 | 0.007 | 15/47 (BT-474, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +3.7 | 0.009 | 10/48 (Hs 766T, A549, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.009 | 5/48 (A498, C-33 A, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.013 | 11/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.020 | 15/46 (HT-29, SHP-77, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.022 | 8/48 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.036 | 9/48 (A498, NCI-H460, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.041 | 8/45 (NCI-H2030, AN3 CA, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.058 | 12/46 (SW480, KATO III, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15405.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (LoVo 0.137×, KATO III 0.150×, C-33 A 0.107×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Nafamostat (mesylate) (drug)]] 0.05 µM in 1 line (RKO 0.0475×); [[Harringtonine (drug)]] 0.05 µM in 1 line (A549 0.0666×); [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (SHP-77 0.0861×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.600×** | -6.3 | 1e-07 | 25/46 (LoVo, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.637×** | -5.6 | 6e-06 | 24/47 (PANC-1, SW480, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.648×** | -5.4 | 1e-05 | 19/46 (PANC-1, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.661×** | -5.1 | 4e-05 | 23/46 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.671×** | -4.8 | 2e-04 | 16/46 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.696×** | -4.5 | 7e-04 | 21/47 (HCT15, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.709×** | -4.3 | 0.002 | 16/46 (BT-474, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15405. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 9.08 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.67× (z +13.8) | [[Decitabine (drug)]] 0.05 µM 0.0973× (z -9.2) |
| [[HS-578T (line)]] | alt | 5.04 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +12.5) | [[Ixazomib (drug)]] 0.05 µM 0.0702× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 5.21 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +13.3) | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0841× (z -9.4) |
| [[SW1417 (line)]] | alt | 11.3 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.69× (z +12.0) | — |
| [[SW480 (line)]] | alt | 9.24 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.61× (z +15.9) | — |
| [[A-172 (line)]] | wt | 12.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.05× (z +16.4) | — |
| [[A549 (line)]] | wt | 6.82 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.95× (z +13.4) | [[Harringtonine (drug)]] 0.05 µM 0.0666× (z -10.4) |
| [[C-33 A (line)]] | alt | 13.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.95× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.107× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[HCT15 (line)]] | alt | 17.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.32× (z +10.6) | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.116× (z -8.8) |
| [[HOP62 (line)]] | alt | 6.83 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +15.6) | — |
| [[HT-29 (line)]] | alt | 9.18 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.21× (z +13.1) | — |
| [[KATO III (line)]] | alt | 10.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +10.7) | [[Digitoxin (drug)]] 5 µM 0.150× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[LoVo (line)]] | wt | 10.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.25× (z +15.4) | [[Digitoxin (drug)]] 5 µM 0.137× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[NCI-H460 (line)]] | wt | 6.75 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.92× (z +14.0) | — |
| [[Panc 03.27 (line)]] | alt | 5.14 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.14× (z +11.2) | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0714× (z -9.5) |
| [[RKO (line)]] | wt | 6.24 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +11.4) | [[Nafamostat (mesylate) (drug)]] 0.05 µM 0.0475× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 7.81 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.53× (z +8.8) | [[Bortezomib (drug)]] 0.05 µM 0.0718× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 8.25 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.71× (z +9.9) | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0861× (z -9.9) |
| [[SNU-423 (line)]] | alt | 7.15 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.65× (z +12.9) | — |
| [[A498 (line)]] | wt | 11.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.16× (z +15.7) | — |
| [[AsPC-1 (line)]] | alt | 7.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +12.7) | — |
| [[C32 (line)]] | wt | 5.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.18× (z +11.2) | — |
| [[CFPAC-1 (line)]] | alt | 7.01 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.80× (z +14.4) | — |
| [[COLO 205 (line)]] | alt | 9.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.19× (z +11.2) | — |
| [[H4 (line)]] | wt | 9.82 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 5 µM 0.0600× (z -9.1) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 12.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.47× (z +14.1) | — |
| [[Hs 766T (line)]] | wt | 9.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.20× (z +13.6) | — |
| [[hTERT-HPNE (line)]] | wt | 7.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.14× (z +9.8) | — |
| [[J82 (line)]] | alt | 6.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.47× (z +11.9) | — |
| [[LS 180 (line)]] | wt | 7.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.25× (z +11.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.42× (z +11.5) | — |
| [[NCI-H1573 (line)]] | alt | 13.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.92× (z +11.2) | — |
| [[NCI-H1792 (line)]] | alt | 6.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.1× (z +13.5) | — |
| [[NCI-H2030 (line)]] | alt | 6.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 7.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.95× (z +12.8) | — |
| [[NCI-H2347 (line)]] | alt | 3.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.91× (z +9.6) | — |
| [[PANC-1 (line)]] | alt | 9.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.57× (z +18.5) | — |
| [[SK-MEL-2 (line)]] | alt | 10.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.23× (z +10.9) | — |
| [[SW 900 (line)]] | alt | 5.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +10.5) | — |
| [[SW48 (line)]] | wt | 9.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.69× (z +9.3) | — |
| [[A-427 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15405), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF3C2-AS2]] | +0.80 | +0.74 / +0.66 | both halves | 7e-06 | same gene group |
| [[MSTO1]] | +0.80 | +0.82 / +0.61 | both halves | 7e-06 |  |
| [[ZNF596]] | +0.79 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[FAM184B]] | +0.79 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[SEC24B-AS1]] | +0.79 | +0.61 / +0.69 | both halves | 7e-06 | same gene group |
| [[SPESP1]] | +0.77 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[ZNF460-AS1]] | +0.77 | +0.56 / +0.69 | both halves | 1e-05 | same gene group |
| [[ZFHX2-AS1]] | +0.77 | +0.73 / +0.49 | both halves | 1e-05 | same gene group |
| [[PRANCR]] | +0.76 | +0.80 / +0.49 | both halves | 1e-05 |  |
| [[CHD1-DT]] | +0.75 | +0.79 / +0.42 | both halves | 4e-05 |  |
| [[SPATA1]] | +0.75 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[PSMD7-DT]] | +0.75 | +0.79 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THEM6]] | -0.66 | -0.32 / -0.54 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZNF213-AS1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.6% of all compounds | 0.006 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[ZNF418]] | B | ZNF418 activity raises ZNF213-AS1's level | lines that do not express ZNF418 (10) vs lines expressing it (40) | 1.09× lower at baseline in the lines without ZNF418 | 0.050 | ⚠ within organs, on part of the lines; also absent: ZNF304, MOCS1, A1BG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.859). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (2.2, 21.3); signed map (27.2, -6.1). **Vector** length 82.1, 15.8% of its response variance represented; |z| ≥ 3 in 986 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.6 | +33.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +16.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +13.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +5.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.6 | +3.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.4 | +3.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | +0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | +0.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | +0.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.3 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | +0.1 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.3 | -1.1 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.3 | -0.7 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | -1.3 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | ZNF213 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 16p13.3 — chr16:3,100,696-3,143,734 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100507458](https://www.ncbi.nlm.nih.gov/gene/100507458):

> Predicted to be involved in SRP-dependent cotranslational protein targeting to membrane, signal sequence recognition. Predicted to be part of signal recognition particle, endoplasmic reticulum targeting. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:50505](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50505) · Entrez [100507458](https://www.ncbi.nlm.nih.gov/gene/100507458) · Ensembl [ENSG00000263072](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000263072)

## Data

Gene col 15405: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15405); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15405, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15405]; `tensor/DDL_lfc|DDL_z.npy` [15405]; `embed/gene_vectors.npy` [15405]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15405 or target_col == 15405). Every well: [[ZNF213-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF213-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
