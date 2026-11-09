---
symbol: "TUBG1"
type: "gene"
col: 5211
ensembl_id: "ENSG00000131462"
name: "tubulin gamma 1"
location: "17q21.31"
module: 6
arm: "+"
pooled_cpm: 12.62
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# TUBG1

*tubulin gamma 1* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.90× (z +12.4, q 2e-32, up in 45 of 46 measured lines) ⚠ cell-cycle shift, explains ~62% of this change. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 2.11× (z +3.6, q 0.012, up in 14 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (J82 0.369×, MIA PaCa-2 0.224×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SW48 0.0768×; ⚠ cell-cycle shift, explains ~18% of this change); [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (C-33 A 0.159×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCF19]] (+0.77, fdr 7e-06), [[ICMT]] (+0.72, fdr 7e-06), [[SIGMAR1]] (+0.70, fdr 7e-06); moves opposite to [[PNISR]] (-0.65, fdr 7e-06), [[CDKL3]] (-0.64, fdr 1e-05), [[EIF3J-DT]] (-0.62, fdr 3e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5211.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **3.90×** | +12.4 | 2e-32 | 45/46 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **3.85×** | +12.3 | 4e-32 | 45/46 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **3.44×** | +11.2 | 5e-27 | 32/36 (A549, A-172, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **3.04×** | +10.1 | 7e-22 | 45/46 (SW480, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **3.02×** | +9.7 | 4e-20 | 19/19 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **2.33×** | +7.7 | 1e-12 | 36/38 (NCI-H2030, Panc 03.27, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.62×** | +6.2 | 4e-08 | 28/44 (A549, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.82×** | +5.5 | 3e-06 | 31/46 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.81×** | +5.2 | 1e-05 | 24/44 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.83×** | +5.1 | 2e-05 | 21/30 (HT-29, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~63% of this change | **1.78×** | +5.0 | 2e-05 | 24/39 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.72×** | +5.0 | 3e-05 | 25/46 (CFPAC-1, A549, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~74% of this change | **1.72×** | +4.8 | 8e-05 | 21/40 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.69×** | +4.6 | 2e-04 | 22/45 (A-172, SNU-423, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.64×** | +4.5 | 2e-04 | 26/44 (HOP62, HT-29, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.11×** | +3.6 | 0.012 | 14/44 (PANC-1, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +3.5 | 0.015 | 18/46 (HOP62, SW 900, …) | two highest doses |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.017 | 18/47 (NCI-H460, NCI-H2030, …) | all doses, flat | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.019 | 15/46 (NCI-H2030, BT-474, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Thymol (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.019 | 17/47 (SK-MEL-2, A-427, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.45×** | +3.4 | 0.020 | 18/47 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.43×** | +3.2 | 0.029 | 12/47 (J82, A-172, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5211.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (J82 0.369×, MIA PaCa-2 0.224×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SW48 0.0768×; ⚠ cell-cycle shift, explains ~18% of this change); [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (C-33 A 0.159×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 0.650× | -3.3 | 0.25 | 17/47 (Hs 766T, A-427, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | 0.504× | -3.2 | 0.25 | 14/46 (HEC-1-A, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.899× | -3.2 | 0.25 | 9/47 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[DTP3 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.709× | -3.1 | 0.27 | 12/46 (LoVo, J82, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.25 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5211. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 11.6 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.80× (z +9.5) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[A549 (line)]] | wt | 7.21 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.8× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | — |
| [[A-172 (line)]] | wt | 25.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | — |
| [[C-33 A (line)]] | alt | 20.7 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.159× (z -8.5) |
| [[J82 (line)]] | alt | 23.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 11.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 9.16 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.04× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | — |
| [[PANC-1 (line)]] | alt | 7.80 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.89× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | — |
| [[SW48 (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0768× (z -8.6) ⚠ cell-cycle shift, explains ~18% of this change |
| [[A-427 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.79 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.26 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5211), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCF19]] | +0.77 | +0.75 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[ICMT]] | +0.72 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[SIGMAR1]] | +0.70 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[GINS2]] | +0.70 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[XRCC3]] | +0.70 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[LSM4]] | +0.70 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[MYCBP]] | +0.69 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[SLC25A39]] | +0.69 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[NAGA]] | +0.68 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[APEH]] | +0.68 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[TUBB]] | +0.68 | +0.76 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS; STRING 629 |
| [[FANCG]] | +0.68 | +0.71 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNISR]] | -0.65 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[CDKL3]] | -0.64 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[EIF3J-DT]] | -0.62 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[SNHG32]] | -0.61 | -0.70 / -0.48 | both halves | 2e-05 |  |
| [[NSA2]] | -0.61 | -0.61 / -0.69 | both halves | 7e-06 |  |
| [[CD72]] | -0.61 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[N4BP2L2]] | -0.60 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[SRSF11]] ⚠ | -0.60 | -0.65 / -0.47 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[N4BP2L1]] | -0.60 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[HSPA2-AS1]] | -0.59 | -0.64 / -0.38 | both halves | 7e-05 |  |
| [[MPHOSPH8]] | -0.59 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[TERF2IP]] | -0.59 | -0.67 / -0.41 | both halves | 4e-05 |  |
| [[UFC1]] | -0.59 | -0.55 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises TUBG1's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.10× lower at baseline in the lines without CDC25A | 0.037 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises TUBG1's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.46× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-33.8, -40.9); signed map (-28.6, -43.1). **Vector** length 85.5, 20.3% of its response variance represented; |z| ≥ 3 in 889 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.55 to 28); *DNA Replication* (reactome, mean cos +0.54 to 40); *E2F G1/S* (control, mean cos +0.54 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | +4.8 | +9.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | +4.2 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | +3.9 | +11.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +3.9 | +12.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +3.8 | +12.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.5 | +3.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | -0.6 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | +1.8 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.3 |
|  | [[Isocorydine (drug)]] 5 µM |  | +1.6 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.8 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -4.9 | -1.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -3.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -2.7 | -3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -1.4 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | -2.2 | -2.8 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.0 | -2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | tubulin gamma 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:42,609,641-42,615,238 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TUBGCP1; previously TUBG |
| Gene groups (HGNC) | Tubulin gamma family |
| Hallmark sets | APICAL_JUNCTION, MTORC1_SIGNALING, E2F_TARGETS |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [P23258](https://www.uniprot.org/uniprotkb/P23258) (Tubulin gamma-1 chain):

> Tubulin is the major constituent of microtubules, protein filaments consisting of alpha- and beta-tubulin heterodimers. Gamma-tubulin is a key component of the gamma-tubulin ring complex (gTuRC) which mediates microtubule nucleation. The gTuRC regulates the minus-end nucleation of alpha-beta tubulin heterodimers that grow into microtubule protafilaments, a critical step in centrosome duplication and spindle formation. Plays a role in sperm morphological development during late stage …

**Summary**, from NCBI Gene [7283](https://www.ncbi.nlm.nih.gov/gene/7283):

> This gene encodes a member of the tubulin superfamily. The encoded protein localizes to the centrosome where it binds to microtubules as part of a complex referred to as the gamma-tubulin ring complex. The protein mediates microtubule nucleation and is required for microtubule formation and progression of the cell cycle. A pseudogene of this gene is found on chromosome 7. [provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:12417](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12417) · Entrez [7283](https://www.ncbi.nlm.nih.gov/gene/7283) · UniProt [P23258](https://www.uniprot.org/uniprotkb/P23258) · Ensembl [ENSG00000131462](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131462)

## Data

Gene col 5211: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5211); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5211, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5211]; `tensor/DDL_lfc|DDL_z.npy` [5211]; `embed/gene_vectors.npy` [5211]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5211 or target_col == 5211). Every well: [[TUBG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUBG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
