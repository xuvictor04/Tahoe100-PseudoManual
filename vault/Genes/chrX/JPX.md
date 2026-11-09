---
symbol: "JPX"
type: "gene"
col: 13460
ensembl_id: "ENSG00000225470"
name: "JPX transcript, XIST activator"
location: "Xq13.2"
module: 1
arm: "+"
pooled_cpm: 141.51
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# JPX

*JPX transcript, XIST activator* — Xq13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.33× (z +6.3, q 2e-07, up in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (KATO III 1.65×, HCT15 2.05×, HT-29 1.71×, NCI-H23 1.60×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (KATO III 1.79×).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.406× (z -27.7, q 0e+00, down in 49 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIGL]] (+0.73, fdr 7e-06), [[COMMD10]] (+0.71, fdr 7e-06), [[TTC27]] (+0.69, fdr 7e-06); moves opposite to [[APAF1]] (-0.67, fdr 7e-06), [[MICA]] (-0.66, fdr 1e-05), [[RUSC1]] (-0.60, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC01535]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13460.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (KATO III 1.65×, HCT15 2.05×, HT-29 1.71×, NCI-H23 1.60×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (KATO III 1.79×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +6.3 | 2e-07 | 32/48 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +6.1 | 3e-07 | 23/48 (KATO III, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.21 | 15/48 (HS-578T, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13460.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.406×** | -27.7 | 0e+00 | 49/49 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.616×** | -10.1 | 2e-21 | 38/48 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.634×** | -9.5 | 4e-19 | 36/47 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.635×** | -9.5 | 4e-19 | 40/50 (RKO, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.723×** | -7.0 | 3e-10 | 36/48 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.746×** | -6.3 | 2e-08 | 28/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.766×** | -5.8 | 7e-07 | 31/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.754×** | -5.6 | 1e-06 | 25/45 (NCI-H23, RKO, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **0.829×** | -4.0 | 0.003 | 25/48 (H4, CHP-212, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | 0.838× | -3.8 | 0.007 | 22/48 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.887× | -3.7 | 0.013 | 10/48 (SK-MEL-2, HEC-1-A, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.955× | -3.1 | 0.079 | 0/50 | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.866× | -3.1 | 0.080 | 14/48 (AN3 CA, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13460. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 172 | 0 | 11 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -26.4) |
| [[PANC-1 (line)]] | alt | 147 | 0 | 9 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -26.2) |
| [[NCI-H23 (line)]] | alt | 182 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +9.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -29.6) |
| [[C-33 A (line)]] | alt | 323 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -15.3) |
| [[MIA PaCa-2 (line)]] | alt | 163 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -13.9) |
| [[SW480 (line)]] | alt | 235 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -19.8) |
| [[RKO (line)]] | wt | 288 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -28.6) |
| [[SW48 (line)]] | wt | 232 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -13.9) |
| [[A-172 (line)]] | wt | 117 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -19.4) |
| [[C32 (line)]] | wt | 84.7 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -20.1) |
| [[HEC-1-A (line)]] | alt | 283 | 0 | 4 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -15.4) |
| [[SK-MEL-2 (line)]] | alt | 204 | 0 | 4 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -16.5) |
| [[AN3 CA (line)]] | alt | 201 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -10.7) |
| [[HOP62 (line)]] | alt | 145 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -20.6) |
| [[HT-29 (line)]] | alt | 154 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -23.8) |
| [[KATO III (line)]] | alt | 157 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -20.1) |
| [[LS 180 (line)]] | wt | 114 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -13.2) |
| [[RPMI-7951 (line)]] | alt | 161 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -17.0) |
| [[SNU-1 (line)]] | wt | 146 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -14.0) |
| [[A-427 (line)]] | wt | 113 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -12.3) |
| [[HCT15 (line)]] | alt | 146 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.278× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 88.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -14.2) |
| [[LoVo (line)]] | wt | 122 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -23.3) |
| [[LOX-IMVI (line)]] | wt | 129 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -21.4) |
| [[Panc 03.27 (line)]] | alt | 125 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -22.4) |
| [[SHP-77 (line)]] | alt | 105 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -8.8) |
| [[SNU-423 (line)]] | alt | 186 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -17.0) |
| [[A498 (line)]] | wt | 134 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -23.4) |
| [[A549 (line)]] | wt | 117 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -19.2) |
| [[AsPC-1 (line)]] | alt | 124 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -21.3) |
| [[CFPAC-1 (line)]] | alt | 77.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -10.1) |
| [[COLO 205 (line)]] | alt | 124 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -11.9) |
| [[H4 (line)]] | wt | 125 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -17.2) |
| [[HepG2_C3A (line)]] | wt | 93.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -13.8) |
| [[Hs 766T (line)]] | wt | 123 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -23.9) |
| [[HS-578T (line)]] | alt | 68.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -11.9) |
| [[J82 (line)]] | alt | 135 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -19.9) |
| [[NCI-H1573 (line)]] | alt | 118 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -13.4) |
| [[NCI-H1792 (line)]] | alt | 109 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -16.8) |
| [[NCI-H2030 (line)]] | alt | 53.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -12.4) |
| [[NCI-H2347 (line)]] | alt | 76.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -11.2) |
| [[SW 1088 (line)]] | alt | 101 | 0 | 1 | — | [[Dexamethasone (drug)]] 5 µM 0.0757× (z -10.1) |
| [[SW 1271 (line)]] | alt | 107 | 0 | 1 | — | [[Cinacalcet (drug)]] 0.5 µM 0.173× (z -8.7) |
| [[SW1417 (line)]] | alt | 96.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -16.0) |
| [[BT-474 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13460), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGL]] | +0.73 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[COMMD10]] | +0.71 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[TTC27]] | +0.69 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[ZC3HC1]] | +0.69 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[ABCE1]] | +0.68 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[DNAJC11]] | +0.68 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[GCFC2]] | +0.67 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[NOL8]] | +0.67 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[ANAPC7]] | +0.67 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[RPL7L1]] | +0.67 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[LDAH]] | +0.66 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[ERCC4]] | +0.66 | +0.76 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APAF1]] | -0.67 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[MICA]] | -0.66 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[RUSC1]] | -0.60 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[OAT]] | -0.60 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[IDH2]] | -0.60 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[ABHD12]] | -0.59 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[MED26]] | -0.58 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[MLF2]] | -0.58 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[FUCA1]] | -0.58 | -0.40 / -0.61 | both halves | 5e-05 |  |
| [[NPTN]] | -0.58 | -0.58 / -0.57 | both halves | 9e-06 |  |
| [[GMCL1]] | -0.58 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[KMT5C]] | -0.57 | -0.60 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01535]] | B | LINC01535 activity raises JPX's level | lines that do not express LINC01535 (21) vs lines expressing it (29) | 1.28× lower at baseline in the lines without LINC01535 | 0.042 | ⚠ within organs, on part of the lines; also absent: MIR3681HG, AFF3, KCNJ6 |
| [[TOP2A]] | B | TOP2A activity raises JPX's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.683). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-22.9, 13.6); signed map (5.7, -42.6). **Vector** length 124, 38.8% of its response variance represented; |z| ≥ 3 in 970 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.4 | +6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.0 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.5 | +2.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +0.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.2 | +2.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.1 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.7 | -27.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -9.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -10.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | -3.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.6 | -3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.6 | -1.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.4 | -1.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | JPX transcript, XIST activator |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | Xq13.2 — chrX:73,944,182-74,070,408 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ENOX, LINC00183, DCBALD06; previously NCRNA00183 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [554203](https://www.ncbi.nlm.nih.gov/gene/554203):

> JPX is a nonprotein-coding RNA transcribed from a gene within the X-inactivation center (XIC; MIM 314670) that appears to participate in X chromosome inactivation (Tian et al., 2010 [PubMed 21029862]).[supplied by OMIM, Feb 2011]

**Accessions** — [HGNC:37191](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37191) · Entrez [554203](https://www.ncbi.nlm.nih.gov/gene/554203) · Ensembl [ENSG00000225470](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225470)

## Data

Gene col 13460: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13460); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13460, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13460]; `tensor/DDL_lfc|DDL_z.npy` [13460]; `embed/gene_vectors.npy` [13460]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13460 or target_col == 13460). Every well: [[JPX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JPX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
