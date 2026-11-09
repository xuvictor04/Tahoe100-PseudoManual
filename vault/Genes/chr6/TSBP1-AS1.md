---
symbol: "TSBP1-AS1"
type: "gene"
col: 13495
ensembl_id: "ENSG00000225914"
name: "TSBP1 and BTNL2 antisense RNA 1"
location: "6p21.32"
module: 15
arm: "+"
pooled_cpm: 11.13
n_lines_expressing: 40
n_dd_up: 19
n_dd_down: 36
n_dd_up_clean: 16
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# TSBP1-AS1

*TSBP1 and BTNL2 antisense RNA 1* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.05× (z +27.0, q 0e+00, up in 28 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.529× (z -8.6, q 3e-15, down in 23 of 37 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.570× (z -7.6, q 8e-12, down in 19 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HLA-DMA]] (+0.66, fdr 1e-05), [[SNX31]] (+0.63, fdr 1e-05), [[TMEM269]] (+0.62, fdr 7e-06); moves opposite to [[WDR7]] (-0.56, fdr 4e-04), [[RITA1]] (-0.54, fdr 5e-05), [[HERC2]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ALG1L9P]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13495.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.05×** | +27.0 | 0e+00 | 28/34 (HS-578T, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.96×** | +14.8 | 0e+00 | 27/36 (J82, SNU-423, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.89×** | +12.4 | 9e-33 | 19/34 (NCI-H23, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **3.65×** | +9.2 | 4e-18 | 21/36 (HEC-1-A, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +8.5 | 1e-15 | 14/34 (C32, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +7.8 | 7e-13 | 18/31 (HEC-1-A, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.67×** | +7.0 | 1e-10 | 16/38 (LoVo, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +7.0 | 2e-10 | 17/38 (HEC-1-A, SK-MEL-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +6.3 | 2e-08 | 14/33 (SW48, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +6.3 | 2e-08 | 3/15 (HEC-1-A, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +5.7 | 7e-07 | 12/37 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +5.3 | 5e-06 | 10/35 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +4.8 | 6e-05 | 7/35 (J82, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +4.6 | 1e-04 | 9/37 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Arbutin (drug)]] 0.05 µM |  | **1.33×** | +3.7 | 0.009 | 4/35 (HEC-1-A, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Cysteamine (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.011 | 1/34 (LoVo) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.051 | 5/37 (SK-MEL-2, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13495.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.529×** | -8.6 | 3e-15 | 23/37 (Hs 766T, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.570×** | -7.6 | 8e-12 | 19/38 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.641×** | -6.0 | 3e-07 | 18/37 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.661×** | -5.6 | 3e-06 | 15/37 (COLO 205, SW480, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.662×** | -5.4 | 8e-06 | 17/35 (COLO 205, SW480, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.755×** | -5.4 | 8e-06 | 10/38 (A549, HEC-1-A, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.508×** | -4.8 | 1e-04 | 10/31 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **0.733×** | -4.2 | 0.002 | 9/38 (SW480, COLO 205, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.734×** | -4.2 | 0.002 | 12/37 (HEC-1-A, CHP-212, …) | two highest doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.740×** | -4.1 | 0.003 | 9/38 (HCT15, KATO III, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.735×** | -4.0 | 0.003 | 13/37 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.752×** | -3.8 | 0.006 | 16/36 (SW480, PANC-1, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **0.744×** | -3.8 | 0.006 | 9/35 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[crizotinib (drug)]] 5 µM |  | **0.748×** | -3.8 | 0.007 | 5/38 (A549, HT-29, …) | top dose only | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **0.595×** | -3.7 | 0.009 | 11/31 (HEC-1-A, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.826×** | -3.6 | 0.010 | 11/38 (SNU-1, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13495. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 25.4 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0676× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.0787× (z -14.9) |
| [[NCI-H23 (line)]] | alt | 59.9 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +10.6) | [[Belinostat (drug)]] 5 µM 0.167× (z -12.6) |
| [[PANC-1 (line)]] | alt | 33.6 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.229× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.293× (z -9.1) |
| [[COLO 205 (line)]] | alt | 26.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0534× (z -14.4) |
| [[HEC-1-A (line)]] | alt | 24.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +10.5) | [[TAK-901 (drug)]] 0.05 µM 0.215× (z -10.8) |
| [[HOP62 (line)]] | alt | 9.41 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +9.0) | [[Radotinib (drug)]] 0.5 µM 0.137× (z -9.1) |
| [[HS-578T (line)]] | alt | 6.64 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.83× (z +12.0) | [[Trifluridine (drug)]] 0.5 µM 0.103× (z -9.3) ⚠ cell-cycle shift, explains ~12% of this change |
| [[LOX-IMVI (line)]] | wt | 4.03 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.60× (z +11.2) | [[Cepharanthine (drug)]] 0.5 µM 0.0679× (z -9.3) |
| [[A-172 (line)]] | wt | 32.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +8.7) | — |
| [[A498 (line)]] | wt | 2.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.14× (z +10.5) | — |
| [[A549 (line)]] | wt | 4.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.99× (z +9.5) | — |
| [[C32 (line)]] | wt | 5.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +11.5) | — |
| [[Hs 766T (line)]] | wt | 16.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0901× (z -10.0) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 6.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.69× (z +10.1) | — |
| [[LoVo (line)]] | wt | 5.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 10.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 15.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -10.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 5.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.7× (z +10.5) | — |
| [[A-427 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13495), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HLA-DMA]] | +0.66 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[SNX31]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[TMEM269]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[ALG1L9P]] | +0.61 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[LINC01482]] | +0.60 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[SPESP1]] | +0.59 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[TMEM91]] | +0.59 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ITFG2-AS1]] | +0.59 | +0.53 / +0.51 | both halves | 1e-05 | same gene group |
| [[SNED1-AS1]] | +0.59 | +0.63 / +0.60 | both halves | 7e-06 | same gene group |
| [[LNP1]] | +0.59 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[DDX59-AS1]] | +0.59 | +0.57 / +0.43 | both halves | 3e-05 | same gene group |
| [[BORCS7-ASMT]] | +0.58 | +0.58 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR7]] | -0.56 | -0.25 / -0.57 | both halves | 4e-04 |  |
| [[RITA1]] | -0.54 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[HERC2]] | -0.54 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[GRHPR]] | -0.52 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[GNPTAB]] | -0.51 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[RAD54L2]] | -0.51 | -0.21 / -0.62 | both halves | 6e-04 |  |
| [[DIS3L2]] | -0.51 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[MRTFB]] | -0.51 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[ELAC2]] | -0.50 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TSBP1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01482]] | B | LINC01482 activity raises TSBP1-AS1's level | lines that do not express LINC01482 (5) vs lines expressing it (45) | 2.22× lower at baseline in the lines without LINC01482 | 0.087 | ⚠ within organs, on part of the lines; also absent: MAP7D2, SLC35F4, ENSG00000226965; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALG1L9P]] | B | TSBP1-AS1 activity raises ALG1L9P's level | lines that do not express TSBP1-AS1 (10) vs lines expressing it (40) | 1.45× lower at baseline in the lines without TSBP1-AS1 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000288993; maybe low, not absent |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.497). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (26.9, -17.6); signed map (11.5, 4.6). **Vector** length 71.8, 13.2% of its response variance represented; |z| ≥ 3 in 919 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +27.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.1 | +14.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +12.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +5.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +0.3 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -6.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -8.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -3.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.9 | -3.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.7 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -4.8 |
|  | [[EX229 (drug)]] 5 µM |  | -1.6 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | TSBP1 and BTNL2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6p21.32 — chr6:32,254,640-32,407,763 (+) |
| Ensembl biotype | lncRNA |
| Also known as | XXbac-BPG154L12.4 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:39756](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:39756) · Entrez [101929163](https://www.ncbi.nlm.nih.gov/gene/101929163) · Ensembl [ENSG00000225914](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225914)

## Data

Gene col 13495: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13495); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13495, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13495]; `tensor/DDL_lfc|DDL_z.npy` [13495]; `embed/gene_vectors.npy` [13495]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13495 or target_col == 13495). Every well: [[TSBP1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSBP1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
