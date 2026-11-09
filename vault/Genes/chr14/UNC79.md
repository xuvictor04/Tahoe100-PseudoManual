---
symbol: "UNC79"
type: "gene"
col: 5489
ensembl_id: "ENSG00000133958"
name: "unc-79 subunit of NALCN channel complex"
location: "14q32.12"
module: 26
arm: "+"
pooled_cpm: 7.94
n_lines_expressing: 49
n_dd_up: 47
n_dd_down: 8
n_dd_up_clean: 43
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# UNC79

*unc-79 subunit of NALCN channel complex* — 14q32.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 47 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.55× (z +27.9, q 0e+00, up in 38 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.616× (z -4.8, q 8e-04, down in 16 of 44 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEB]] (+0.83, fdr 7e-06), [[INTS6-AS1]] (+0.81, fdr 7e-06), [[CHODL]] (+0.81, fdr 7e-06).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[KATNAL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 47 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5489.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.55×** | +27.9 | 0e+00 | 38/40 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.25×** | +21.5 | 0e+00 | 39/41 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.14×** | +11.6 | 1e-28 | 27/35 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.73×** | +10.5 | 8e-24 | 32/38 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.77×** | +10.3 | 8e-23 | 28/40 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.57×** | +9.9 | 3e-21 | 27/44 (HOP62, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.90×** | +9.6 | 9e-20 | 32/45 (NCI-H460, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.17×** | +8.2 | 2e-14 | 32/47 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.26×** | +7.9 | 1e-13 | 4/13 (NCI-H1573, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.68×** | +7.7 | 6e-13 | 21/46 (CFPAC-1, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.98×** | +6.9 | 2e-10 | 8/23 (MIA PaCa-2, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.92×** | +6.9 | 3e-10 | 23/44 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.90×** | +6.8 | 6e-10 | 13/22 (LOX-IMVI, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.89×** | +6.7 | 8e-10 | 24/47 (MIA PaCa-2, NCI-H2030, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +6.4 | 5e-09 | 20/46 (HOP62, A549, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.88×** | +6.4 | 6e-09 | 16/44 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.82×** | +6.3 | 1e-08 | 22/44 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.83×** | +6.1 | 4e-08 | 21/46 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5489.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.616×** | -4.8 | 8e-04 | 16/44 (SW48, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.651×** | -4.3 | 0.005 | 15/45 (LOX-IMVI, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.689×** | -3.7 | 0.030 | 14/44 (NCI-H460, SW480, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **0.705×** | -3.7 | 0.030 | 8/44 (HS-578T, A549, …) | all doses, flat | position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.783×** | -3.6 | 0.030 | 9/47 (LoVo, LOX-IMVI, …) | all doses, flat | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.712×** | -3.6 | 0.032 | 16/46 (NCI-H460, SW48, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.725×** | -3.4 | 0.058 | 12/46 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.732×** | -3.3 | 0.072 | 6/43 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.912× | -3.0 | 0.15 | 14/47 (A-172, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5489. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 142 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.154× (z -15.5) |
| [[MIA PaCa-2 (line)]] | alt | 10.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.92× (z +11.5) | — |
| [[A498 (line)]] | wt | 6.49 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 17.1× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 15.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +11.1) | — |
| [[SW480 (line)]] | alt | 6.44 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +12.4) | — |
| [[HEC-1-A (line)]] | alt | 6.42 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.10× (z +11.9) | — |
| [[Hs 766T (line)]] | wt | 5.31 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.28× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 3.63 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +9.6) | — |
| [[A-172 (line)]] | wt | 2.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.75× (z +8.8) | — |
| [[A549 (line)]] | wt | 2.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.8× (z +11.2) | — |
| [[BT-474 (line)]] | alt | 2.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.0× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 4.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.66× (z +10.8) | — |
| [[HCT15 (line)]] | alt | 4.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +8.9) | — |
| [[HOP62 (line)]] | alt | 3.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.68× (z +12.2) | — |
| [[HS-578T (line)]] | alt | 2.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.20× (z +8.9) | — |
| [[LoVo (line)]] | wt | 5.46 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0428× (z -13.5) |
| [[LOX-IMVI (line)]] | wt | 2.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.26× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 11.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +12.3) | — |
| [[Panc 03.27 (line)]] | alt | 2.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.1× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 3.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.09× (z +11.8) | — |
| [[RPMI-7951 (line)]] | alt | 6.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.68× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 4.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.29× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 2.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +9.3) | — |
| [[SW48 (line)]] | wt | 21.5 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0657× (z -8.8) |
| [[A-427 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5489), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEB]] | +0.83 | +0.86 / +0.63 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.81 | +0.83 / +0.62 | both halves | 7e-06 |  |
| [[CHODL]] | +0.81 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.81 | +0.84 / +0.57 | both halves | 1e-05 |  |
| [[USP38-DT]] | +0.79 | +0.79 / +0.64 | both halves | 7e-06 |  |
| [[H2AZ1-DT]] | +0.79 | +0.83 / +0.66 | both halves | 7e-06 |  |
| [[LINC00240]] | +0.79 | +0.81 / +0.59 | both halves | 7e-06 |  |
| [[OXA1L-DT]] | +0.78 | +0.81 / +0.50 | both halves | 1e-05 |  |
| [[DNAH12]] | +0.77 | +0.80 / +0.65 | both halves | 7e-06 |  |
| [[DRAIC]] | +0.77 | +0.79 / +0.56 | both halves | 1e-05 |  |
| [[GUCY2C-AS1]] | +0.76 | +0.77 / +0.57 | both halves | 1e-05 |  |
| [[PCNX4-DT]] | +0.76 | +0.82 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KATNAL2]] | B | KATNAL2 activity raises UNC79's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 1.85× lower at baseline in the lines without KATNAL2 | 0.065 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises UNC79's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers UNC79's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.4% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[H2AJ]] | B | H2AJ activity lowers UNC79's level | lines that do not express H2AJ (11) vs lines expressing it (39) | 1.99× higher at baseline in the lines without H2AJ | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321 |
| [[SYNPO2]] | B | SYNPO2 activity lowers UNC79's level | lines that do not express SYNPO2 (5) vs lines expressing it (45) | 1.86× higher at baseline in the lines without SYNPO2 | 0.091 | ⚠ within organs, on part of the lines; also absent: RIPOR3, PER3, TESK2; maybe low, not absent |
| [[LINC00882]] | B | LINC00882 activity raises UNC79's level | lines that do not express LINC00882 (17) vs lines expressing it (33) | 1.65× lower at baseline in the lines without LINC00882 | 0.097 | ⚠ within organs, on part of the lines; also absent: TUSC3, B3GALT1, EVC |
| [[LINC02307]] | C | LINC02307's natural level weakens UNC79's drug response | LINC02307's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.67, reverse -0.43; direction clear | 0.032 | ⚠ tissue can mimic it; precision caveat |
| [[CNTNAP5]] | C | CNTNAP5's natural level weakens UNC79's drug response | CNTNAP5's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.10; direction clear | 0.043 | ⚠ tissue can mimic it; precision caveat |
| [[LINC02306]] | C | LINC02306's natural level weakens UNC79's drug response | LINC02306's natural level across 35 lines (lineage-adjusted; a glimpse) | r -0.77, reverse -0.56; direction not clear | 0.048 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.761). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.8, 17.3); signed map (28.9, -4.9). **Vector** length 74.2, 13.3% of its response variance represented; |z| ≥ 3 in 1,108 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.1 | +21.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +27.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.8 | +10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +6.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +6.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -3.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.1 | +4.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.6 | -3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.6 | -2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -3.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | unc-79 subunit of NALCN channel complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.12 — chr14:93,333,219-93,707,876 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA1409 |
| Gene groups (HGNC) | Armadillo like helical domain containing; NALCN channel complex subunits |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2D8](https://www.uniprot.org/uniprotkb/Q9P2D8) (Protein unc-79 homolog):

> Auxilary subunit of the NALCN channelosome complex, which regulates the resting membrane potential by depolarizing sodium leak currents. The NALCN channelosome complex is a voltage-gated ion channel responsible for the resting Na(+) permeability that controls neuronal excitability. The NALCN channelosome is constitutively active and conducts monovalent cations but is blocked by physiological concentrations of extracellular divalent cations. Activated by neuropeptides substance P, neurotensin, …

**Summary**, from NCBI Gene [57578](https://www.ncbi.nlm.nih.gov/gene/57578):

> The NALCN channel is responsible for Na(+) leak currents. The protein encoded by this gene, along with UNC80, is an accessory subunit of the NALCN channel that contributes to the Ca(2+) sensitivity of the channel. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:19966](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19966) · Entrez [57578](https://www.ncbi.nlm.nih.gov/gene/57578) · UniProt [Q9P2D8](https://www.uniprot.org/uniprotkb/Q9P2D8) · Ensembl [ENSG00000133958](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133958)

## Data

Gene col 5489: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5489); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5489, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5489]; `tensor/DDL_lfc|DDL_z.npy` [5489]; `embed/gene_vectors.npy` [5489]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5489 or target_col == 5489). Every well: [[UNC79 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UNC79.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
