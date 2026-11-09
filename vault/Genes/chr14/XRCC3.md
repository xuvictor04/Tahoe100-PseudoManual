---
symbol: "XRCC3"
type: "gene"
col: 4719
ensembl_id: "ENSG00000126215"
name: "X-ray repair cross complementing 3"
location: "14q32.33"
module: 6
arm: "+"
pooled_cpm: 6.74
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 6
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 11
direction_downstream: 1
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# XRCC3

*X-ray repair cross complementing 3* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (20 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.52× (z +17.1, q 0e+00, up in 34 of 40 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.42× (z +4.4, q 4e-04, up in 9 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.780× (z -4.6, q 0.002, down in 11 of 47 measured lines) ⚠ cell-cycle shift, explains ~78% of this change. The strongest without an alert is [[Niclosamide (olamine) (drug)]] 0.5 µM: 0.737× (z -4.0, q 0.008, down in 7 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 0.150×, KATO III 0.207×; ⚠ cell-cycle shift, explains ~17% of this change); [[PF-06260933 (drug)]] 5 µM in 1 line (PANC-1 0.0587×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (BT-474 0.0867×); [[Oxaprozin (drug)]] 0.5 µM in 1 line (A-172 0.105×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC45]] (+0.87, fdr 7e-06), [[PKMYT1]] (+0.87, fdr 7e-06), [[TONSL]] (+0.87, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); 1 goes from it, the strongest it → [[WDR76]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 21 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4719.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.52×** | +17.1 | 0e+00 | 34/40 (PANC-1, SW1417, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **3.58×** | +16.7 | 0e+00 | 44/47 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **3.46×** | +16.2 | 0e+00 | 25/28 (SW480, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **2.96×** | +14.2 | 2e-43 | 43/47 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **3.06×** | +14.1 | 5e-43 | 11/12 (SW480, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **2.56×** | +12.3 | 9e-33 | 42/47 (SW480, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **2.66×** | +11.8 | 3e-30 | 12/15 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **2.41×** | +11.1 | 1e-26 | 21/33 (SW480, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **2.01×** | +8.8 | 1e-16 | 25/38 (SW480, PANC-1, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.89×** | +8.0 | 6e-14 | 25/43 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.84×** | +8.0 | 7e-14 | 24/47 (J82, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.67×** | +6.7 | 1e-09 | 20/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.31×** | +5.0 | 2e-05 | 13/46 (NCI-H2347, SHP-77, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +4.5 | 2e-04 | 6/33 (NCI-H2347, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.42×** | +4.4 | 4e-04 | 9/44 (NCI-H23, NCI-H2347, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.3 | 6e-04 | 10/48 (NCI-H2347, CFPAC-1, …) | rises with dose | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.84×** | +4.2 | 9e-04 | 9/38 (NCI-H460, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.35×** | +3.6 | 0.008 | 11/36 (PANC-1, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[Gemcitabine (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.010 | 1/42 (C-33 A) | rises with dose | noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.016 | 6/47 (NCI-H2030, HOP62, …) | top dose only | plate-row cell shift |
| [[venetoclax (drug)]] 5 µM |  | **1.64×** | +3.4 | 0.016 | 7/34 (NCI-H460, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Irinotecan (drug)]] 5 µM |  | **1.58×** | +3.1 | 0.037 | 1/45 (A-427) | rises with dose | noisy plate (z scaled) |
| [[Flutamide (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.045 | 4/42 (C-33 A, SW1417, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.53×** | +2.9 | 0.066 | 1/36 (NCI-H460) | inconsistent across doses | noisy plate (z scaled) |
| [[Larotrectinib (drug)]] 5 µM |  | 1.17× | +2.9 | 0.075 | 5/46 (NCI-H460, KATO III, …) | top dose only | position effect removed |
| [[EX229 (drug)]] 0.5 µM |  | **1.35×** | +2.8 | 0.083 | 2/46 (MIA PaCa-2, J82) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4719.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 0.150×, KATO III 0.207×; ⚠ cell-cycle shift, explains ~17% of this change); [[PF-06260933 (drug)]] 5 µM in 1 line (PANC-1 0.0587×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (BT-474 0.0867×); [[Oxaprozin (drug)]] 0.5 µM in 1 line (A-172 0.105×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.780×** | -4.6 | 0.002 | 11/47 (HCT15, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.790×** | -4.4 | 0.003 | 21/46 (A498, NCI-H460, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.731×** | -4.1 | 0.007 | 15/44 (A-427, A498, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.737×** | -4.0 | 0.008 | 7/47 (SK-MEL-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.741×** | -3.9 | 0.010 | 15/38 (NCI-H23, KATO III, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.764×** | -3.5 | 0.038 | 9/46 (MIA PaCa-2, NCI-H1573, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.940× | -3.1 | 0.17 | 5/48 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.32 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4719. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 9.18 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.13× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[Panc 03.27 (line)]] | alt | 9.29 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +9.9) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[PANC-1 (line)]] | alt | 6.33 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +10.0) ⚠ cell-cycle shift, explains ~35% of this change | [[PF-06260933 (drug)]] 5 µM 0.0587× (z -8.9) |
| [[A-172 (line)]] | wt | 5.11 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.105× (z -8.6) |
| [[A498 (line)]] | wt | 4.25 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.269× (z -8.5) ⚠ cell-cycle shift, explains ~38% of this change |
| [[BT-474 (line)]] | alt | 8.95 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0867× (z -8.8) |
| [[KATO III (line)]] | alt | 9.73 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -9.6) ⚠ cell-cycle shift, explains ~17% of this change |
| [[NCI-H23 (line)]] | alt | 6.83 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -10.4) ⚠ cell-cycle shift, explains ~17% of this change |
| [[SW1417 (line)]] | alt | 10.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +10.0) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[A-427 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.67 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4719), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC45]] | +0.87 | +0.87 / +0.85 | both halves | 7e-06 |  |
| [[PKMYT1]] | +0.87 | +0.84 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[TONSL]] | +0.87 | +0.85 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[E2F1]] | +0.87 | +0.86 / +0.87 | both halves | 7e-06 |  |
| [[CLSPN]] | +0.86 | +0.88 / +0.84 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair |
| [[FANCA]] | +0.86 | +0.85 / +0.83 | both halves | 7e-06 | STRING 799 |
| [[MCM4]] | +0.84 | +0.85 / +0.81 | both halves | 7e-06 | STRING 472 |
| [[MCM10]] | +0.84 | +0.83 / +0.84 | both halves | 7e-06 |  |
| [[MYBL2]] | +0.84 | +0.83 / +0.83 | both halves | 7e-06 |  |
| [[RAD54L]] | +0.83 | +0.79 / +0.82 | both halves | 7e-06 | STRING 758 |
| [[GINS2]] | +0.83 | +0.81 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[MCM3]] | +0.82 | +0.87 / +0.78 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 7, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises XRCC3's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.26× lower at baseline in the lines without E2F8 | 0.014 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises XRCC3's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.77× lower at baseline in the lines without CDC25A | 0.026 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises XRCC3's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.70× lower at baseline in the lines without E2F2 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[FAM111B]] | B | FAM111B activity raises XRCC3's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.63× lower at baseline in the lines without FAM111B | 0.053 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers XRCC3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TCF19]] | B | TCF19 activity raises XRCC3's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 1.90× lower at baseline in the lines without TCF19 | 0.066 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers XRCC3's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 6.4% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[BRME1]] | C | BRME1 activity raises XRCC3's level | lines that do not express BRME1 (4) vs lines expressing it (46) | 1.88× lower at baseline in the lines without BRME1 | 0.036 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, NRTN, TENT5C; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises XRCC3's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.07× lower at baseline in the lines without DSCC1 | 0.037 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[CLSPN]] | C | CLSPN activity raises XRCC3's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 2.13× lower at baseline in the lines without CLSPN | 0.063 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent |
| [[CDC45]], [[CENPM]] | C | CDC45, CENPM activity raises XRCC3's level | lines that do not express CDC45, CENPM (3) vs lines expressing them (47) | 2.28× lower at baseline in the lines without CDC45, CENPM | 0.069 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent genes |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WDR76]] | C | XRCC3's natural level weakens WDR76's drug response | XRCC3's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.71, reverse -0.19; direction not clear | 0.014 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.866). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.3, -43.9); signed map (-37.2, -45.7). **Vector** length 80.7, 15.5% of its response variance represented; |z| ≥ 3 in 1,018 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.65 to 65); *DNA strand elongation* (reactome, mean cos +0.72 to 28); *DNA Replication* (reactome, mean cos +0.71 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | +5.4 | +16.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | +5.4 | +14.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | +4.4 | +11.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.1 | +17.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +3.9 | +8.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +2.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.8 | +2.9 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -4.1 | -4.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.9 | -4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -3.8 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -3.5 | -3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -0.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -2.5 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -1.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | X-ray repair cross complementing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:103,697,609-103,715,504 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RAD51 paralogs |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Reactome | 9 pathways, smallest: Resolution of D-loop Structures through Synthesis-Dependent Strand Annealing (SDSA); Resolution of D-loop Structures through Holliday Junction Intermediates; Resolution of D-Loop Structures |
| Matched by | ensembl_id |

**Function**, from UniProt [O43542](https://www.uniprot.org/uniprotkb/O43542) (DNA repair protein XRCC3):

> Involved in the homologous recombination repair (HRR) pathway of double-stranded DNA, thought to repair chromosomal fragmentation, translocations and deletions. Part of the RAD51 paralog protein complex CX3 which acts in the BRCA1-BRCA2-dependent HR pathway. Upon DNA damage, CX3 acts downstream of RAD51 recruitment; the complex binds predominantly to the intersection of the four duplex arms of the Holliday junction (HJ) and to junctions of replication forks. Involved in HJ resolution and thus …

**Summary**, from NCBI Gene [7517](https://www.ncbi.nlm.nih.gov/gene/7517):

> This gene encodes a member of the RecA/Rad51-related protein family that participates in homologous recombination to maintain chromosome stability and repair DNA damage. This gene functionally complements Chinese hamster irs1SF, a repair-deficient mutant that exhibits hypersensitivity to a number of different DNA-damaging agents and is chromosomally unstable. A rare microsatellite polymorphism in this gene is associated with cancer in patients of varying radiosensitivity. Alternatively spliced …

**Accessions** — [HGNC:12830](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12830) · Entrez [7517](https://www.ncbi.nlm.nih.gov/gene/7517) · UniProt [O43542](https://www.uniprot.org/uniprotkb/O43542) · Ensembl [ENSG00000126215](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126215)

## Data

Gene col 4719: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4719); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4719, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4719]; `tensor/DDL_lfc|DDL_z.npy` [4719]; `embed/gene_vectors.npy` [4719]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4719 or target_col == 4719). Every well: [[XRCC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XRCC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
