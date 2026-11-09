---
symbol: "ISG15"
type: "gene"
col: 11928
ensembl_id: "ENSG00000187608"
name: "ISG15 ubiquitin like modifier"
location: "1p36.33"
module: 70
arm: "+"
pooled_cpm: 108.47
n_lines_expressing: 46
n_dd_up: 6
n_dd_down: 17
n_dd_up_clean: 2
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 25
direction_downstream: 18
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# ISG15

*ISG15 ubiquitin like modifier* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 3.81× (z +7.2, q 3e-10, up in 41 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (AsPC-1 6.40×, LS 180 4.99×, HEC-1-A 3.64×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 0.5 µM in 3 lines (NCI-H460 9.83×, PANC-1 6.00×, COLO 205 8.38×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 13.5×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.421× (z -6.9, q 3e-09, down in 33 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFI6]] (+0.89, fdr 7e-06), [[IFI27]] (+0.87, fdr 7e-06), [[IFITM3]] (+0.86, fdr 7e-06).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[RSAD2]] → it (grade B ⚠); 18 go from it, the strongest it → [[IFIH1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11928.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (AsPC-1 6.40×, LS 180 4.99×, HEC-1-A 3.64×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 0.5 µM in 3 lines (NCI-H460 9.83×, PANC-1 6.00×, COLO 205 8.38×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 13.5×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **3.81×** | +7.2 | 3e-10 | 41/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.84×** | +5.7 | 3e-06 | 30/44 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **2.31×** | +4.8 | 4e-04 | 37/44 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.26×** | +4.6 | 5e-04 | 30/43 (NCI-H460, LS 180, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.04×** | +4.1 | 0.006 | 35/44 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.98×** | +3.9 | 0.010 | 26/44 (LS 180, AsPC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11928.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.421×** | -6.9 | 3e-09 | 33/45 (C-33 A, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.346×** | -6.0 | 5e-07 | 30/45 (SNU-423, C-33 A, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.495×** | -5.6 | 3e-06 | 36/44 (COLO 205, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.514×** | -5.3 | 1e-05 | 29/45 (MIA PaCa-2, COLO 205, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.395×** | -5.3 | 2e-05 | 30/44 (C-33 A, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.462×** | -4.4 | 0.001 | 25/45 (MIA PaCa-2, SHP-77, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | **0.483×** | -4.1 | 0.003 | 34/44 (NCI-H2347, SHP-77, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.252×** | -4.1 | 0.003 | 30/44 (C-33 A, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.252×** | -4.1 | 0.003 | 34/45 (NCI-H2347, C-33 A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.496×** | -4.0 | 0.004 | 31/44 (RPMI-7951, RKO, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.514×** | -3.8 | 0.009 | 34/44 (NCI-H2347, SHP-77, …) | rises with dose | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.549×** | -3.4 | 0.031 | 34/44 (SHP-77, NCI-H1573, …) | all doses, flat | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.319×** | -3.4 | 0.031 | 33/45 (C-33 A, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.552×** | -3.4 | 0.031 | 26/44 (SHP-77, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[crizotinib (drug)]] 5 µM |  | **0.549×** | -3.3 | 0.041 | 29/44 (SNU-423, A498, …) | top dose only |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.342×** | -3.2 | 0.053 | 24/44 (CFPAC-1, COLO 205, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.70 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11928. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 119 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -11.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0822× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 139 | 5 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 13.5× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 9.83× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 136 | 0 | 5 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.120× (z -12.7) |
| [[COLO 205 (line)]] | alt | 113 | 1 | 3 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 8.38× (z +8.5) | [[Tofacitinib (drug)]] 5 µM 0.160× (z -10.9) |
| [[KATO III (line)]] | alt | 96.8 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0725× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.211× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 122 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0368× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.131× (z -12.9) |
| [[NCI-H2347 (line)]] | alt | 423 | 0 | 4 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.193× (z -12.5) |
| [[BT-474 (line)]] | alt | 59.8 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.117× (z -9.1) |
| [[C-33 A (line)]] | alt | 183 | 0 | 3 | — | [[Tofacitinib (drug)]] 5 µM 0.160× (z -13.0) |
| [[NCI-H1792 (line)]] | alt | 84.8 | 0 | 3 | — | [[Tofacitinib (drug)]] 5 µM 0.166× (z -10.3) |
| [[SNU-423 (line)]] | alt | 125 | 0 | 3 | — | [[Tofacitinib (drug)]] 5 µM 0.202× (z -11.1) |
| [[CFPAC-1 (line)]] | alt | 515 | 0 | 2 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.176× (z -13.0) |
| [[HepG2_C3A (line)]] | wt | 183 | 0 | 2 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.213× (z -10.0) |
| [[HS-578T (line)]] | alt | 126 | 0 | 2 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.189× (z -11.1) |
| [[RPMI-7951 (line)]] | alt | 81.3 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.104× (z -10.4) |
| [[A-172 (line)]] | wt | 201 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 81.7 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.277× (z -9.2) |
| [[A549 (line)]] | wt | 80.4 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.207× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 104 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.40× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HEC-1-A (line)]] | alt | 43.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LoVo (line)]] | wt | 156 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.219× (z -9.4) |
| [[LS 180 (line)]] | wt | 180 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 60.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0968× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 41.4 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 6.00× (z +8.6) | — |
| [[A-427 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.1 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 22.5 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.5 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 114 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11928), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFI6]] | +0.89 | +0.83 / +0.90 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 959 |
| [[IFI27]] | +0.87 | +0.79 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 970 |
| [[IFITM3]] | +0.86 | +0.77 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 911 |
| [[IRF7]] | +0.84 | +0.72 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 973 |
| [[OAS1]] | +0.83 | +0.73 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 983 |
| [[RSAD2]] | +0.83 | +0.81 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 978 |
| [[IFIH1]] | +0.82 | +0.76 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 994 |
| [[PSMB9]] | +0.82 | +0.70 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 623 |
| [[IFI44]] | +0.81 | +0.77 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 964 |
| [[PARP9]] | +0.81 | +0.77 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 857 |
| [[HELZ2]] | +0.80 | +0.73 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 829 |
| [[UBE2L6]] | +0.80 | +0.67 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 994 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 18, C 7. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RSAD2]] | B | RSAD2 activity raises ISG15's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.22× lower at baseline in the lines without RSAD2 | 0.003 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[IFI27]] | B | IFI27 activity raises ISG15's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 2.01× lower at baseline in the lines without IFI27 | 0.007 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[ODF3B]] | B | ODF3B activity raises ISG15's level | lines that do not express ODF3B (13) vs lines expressing it (37) | 1.99× lower at baseline in the lines without ODF3B | 0.012 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |
| [[OAS2]] | B | OAS2 activity raises ISG15's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.04× lower at baseline in the lines without OAS2 | 0.012 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[EPSTI1]] | B | EPSTI1 activity raises ISG15's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 2.07× lower at baseline in the lines without EPSTI1 | 0.017 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[RASGRP3]] | B | RASGRP3 activity strengthens ISG15's drug response | lines that do not express RASGRP3 (14) vs lines expressing it (31) | the lines without RASGRP3 respond 0.47× as strongly (z diff +1.66); strongest at Fedratinib (hydrochloride hydrate) 5 µM: 0.88x vs 0.37x (z diff +3.1) | 0.026 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[IFITM1]] | B | IFITM1 activity raises ISG15's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 1.70× lower at baseline in the lines without IFITM1 | 0.030 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[SAMD9L]] | B | SAMD9L activity raises ISG15's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 1.65× lower at baseline in the lines without SAMD9L | 0.033 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[IFIT3]] | B | IFIT3 activity raises ISG15's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 1.53× lower at baseline in the lines without IFIT3 | 0.039 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[IFI44]] | B | IFI44 activity raises ISG15's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 1.58× lower at baseline in the lines without IFI44 | 0.042 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[OAS1]] | B | OAS1 activity raises ISG15's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.23× lower at baseline in the lines without OAS1 | 0.044 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[OASL]] | B | OASL activity raises ISG15's level | lines that do not express OASL (10) vs lines expressing it (40) | 2.31× lower at baseline in the lines without OASL | 0.057 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 0, C 18. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFIH1]] | C | ISG15 activity raises IFIH1's level | lines that do not express ISG15 (4) vs lines expressing it (46) | 3.90× lower at baseline in the lines without ISG15 | 0.007 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFIH1, IFI35, NUTM2A-AS1; maybe low, not absent; co-absent with the target |
| [[RIGI]] | C | ISG15 activity raises RIGI's level | lines that do not express ISG15 (4) vs lines expressing it (46) | 4.01× lower at baseline in the lines without ISG15 | 0.021 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFIH1, IFI35, NUTM2A-AS1; maybe low, not absent |
| [[SP110]] | C | ISG15 activity raises SP110's level | lines that do not express ISG15 (4) vs lines expressing it (46) | 3.56× lower at baseline in the lines without ISG15 | 0.036 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFIH1, IFI35, NUTM2A-AS1; maybe low, not absent |
| [[TAP2]] | C | ISG15 activity raises TAP2's level | lines that do not express ISG15 (4) vs lines expressing it (46) | 2.01× lower at baseline in the lines without ISG15 | 0.038 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFIH1, IFI35, NUTM2A-AS1; maybe low, not absent |
| [[TAP1]] | C | ISG15 activity raises TAP1's level | lines that do not express ISG15 (4) vs lines expressing it (46) | 2.40× lower at baseline in the lines without ISG15 | 0.041 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFIH1, IFI35, NUTM2A-AS1; maybe low, not absent |
| [[SHISA5]] | C | ISG15 activity strengthens SHISA5's drug response | lines that do not express ISG15 (4) vs lines expressing it (45) | the lines without ISG15 respond 0.54× as strongly (z diff +2.51); strongest at Panobinostat 5 µM: 0.78x vs 0.44x (z diff +4.7) | 0.045 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFIH1, IFI35, NUTM2A-AS1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[OAS3]] | C | ISG15 activity raises OAS3's level | lines that do not express ISG15 (4) vs lines expressing it (46) | 3.55× lower at baseline in the lines without ISG15 | 0.053 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFIH1, IFI35, NUTM2A-AS1; maybe low, not absent |
| [[HERC6]] | C | ISG15 activity raises HERC6's level | lines that do not express ISG15 (4) vs lines expressing it (46) | 3.38× lower at baseline in the lines without ISG15 | 0.055 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFIH1, IFI35, NUTM2A-AS1; maybe low, not absent; co-absent with the target |
| [[IFIT1]] | C | ISG15 activity raises IFIT1's level | lines that do not express ISG15 (4) vs lines expressing it (46) | 3.56× lower at baseline in the lines without ISG15 | 0.055 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFIH1, IFI35, NUTM2A-AS1; maybe low, not absent |
| [[TRIM25]] | C | ISG15 activity raises TRIM25's level | lines that do not express ISG15 (4) vs lines expressing it (46) | 2.13× lower at baseline in the lines without ISG15 | 0.057 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFIH1, IFI35, NUTM2A-AS1; maybe low, not absent |
| [[USP18]] | C | ISG15 activity raises USP18's level | lines that do not express ISG15 (4) vs lines expressing it (46) | 2.97× lower at baseline in the lines without ISG15 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFIH1, IFI35, NUTM2A-AS1; maybe low, not absent |
| [[IFI35]] | C | ISG15 activity raises IFI35's level | lines that do not express ISG15 (4) vs lines expressing it (46) | 2.92× lower at baseline in the lines without ISG15 | 0.069 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFIH1, IFI35, NUTM2A-AS1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.798). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (49.2, 51.5); signed map (65.1, 29.1). **Vector** length 156, 62.1% of its response variance represented; |z| ≥ 3 in 1,033 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Antigen processing-Cross presentation* (reactome, mean cos +0.65 to 14); *Interferon gamma signaling* (reactome, mean cos +0.67 to 13); *Endosomal/Vacuolar pathway* (reactome, mean cos +0.63 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.1 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +6.7 | +3.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +5.9 | +5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.4 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.8 | +2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.7 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.6 | +2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.5 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +4.1 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -8.4 | -6.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -7.7 | -5.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -7.2 | -6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.1 | -4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -6.5 | -0.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -6.2 | -5.3 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -5.8 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | ISG15 ubiquitin like modifier |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:1,001,138-1,014,540 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IFI15, UCRP; previously G1P2 |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 23 pathways, smallest: Modulation of host responses by IFN-stimulated genes; Termination of translesion DNA synthesis; Negative regulators of DDX58/IFIH1 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P05161](https://www.uniprot.org/uniprotkb/P05161) (Ubiquitin-like protein ISG15):

> Ubiquitin-like protein which plays a key role in the innate immune response to viral infection either via its conjugation to a target protein (ISGylation) or via its action as a free or unconjugated protein. ISGylation involves a cascade of enzymatic reactions involving E1, E2, and E3 enzymes which catalyze the conjugation of ISG15 to a lysine residue in the target protein. Its target proteins include IFIT1, MX1/MxA, PPM1B, UBE2L6, UBA7, CHMP5, CHMP2A, CHMP4B and CHMP6. Isgylation of the viral …

**Summary**, from NCBI Gene [9636](https://www.ncbi.nlm.nih.gov/gene/9636):

> The protein encoded by this gene is a ubiquitin-like protein that is conjugated to intracellular target proteins upon activation by interferon-alpha and interferon-beta. Several functions have been ascribed to the encoded protein, including chemotactic activity towards neutrophils, direction of ligated target proteins to intermediate filaments, cell-to-cell signaling, and antiviral activity during viral infections. While conjugates of this protein have been found to be noncovalently attached to …

**Accessions** — [HGNC:4053](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4053) · Entrez [9636](https://www.ncbi.nlm.nih.gov/gene/9636) · UniProt [P05161](https://www.uniprot.org/uniprotkb/P05161) · Ensembl [ENSG00000187608](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187608)

## Data

Gene col 11928: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11928); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11928, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11928]; `tensor/DDL_lfc|DDL_z.npy` [11928]; `embed/gene_vectors.npy` [11928]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11928 or target_col == 11928). Every well: [[ISG15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ISG15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
