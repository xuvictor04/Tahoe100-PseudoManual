---
symbol: "DHCR7"
type: "gene"
col: 10312
ensembl_id: "ENSG00000172893"
name: "7-dehydrocholesterol reductase"
location: "11q13.4"
module: 86
arm: "+"
pooled_cpm: 13.29
n_lines_expressing: 47
n_dd_up: 40
n_dd_down: 11
n_dd_up_clean: 33
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# DHCR7

*7-dehydrocholesterol reductase* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (7 with an alert ⚠); the strongest is [[Berbamine (drug)]] 5 µM: 3.02× (z +16.1, q 0e+00, up in 42 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.676× (z -5.8, q 4e-06, down in 25 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMGCR]] (+0.85, fdr 7e-06), [[MSMO1]] (+0.84, fdr 7e-06), [[FDFT1]] (+0.83, fdr 7e-06); moves opposite to [[ZNF830]] (-0.46, fdr 3e-04), [[ZNF721]] (-0.43, fdr 1e-04), [[ALKBH1]] (-0.42, fdr 1e-04).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[QPRT]] → it (grade B ⚠); 3 go from it, the strongest it → cells under [[Topotecan (hydrochloride) (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10312.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Berbamine (drug)]] 5 µM |  | **3.02×** | +16.1 | 0e+00 | 42/44 (HOP62, LoVo, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **3.01×** | +16.0 | 0e+00 | 43/44 (HOP62, NCI-H23, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.49×** | +12.3 | 9e-33 | 20/21 (A-427, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.12×** | +11.7 | 2e-29 | 31/35 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.99×** | +11.2 | 3e-27 | 41/44 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.37×** | +11.2 | 6e-27 | 38/45 (A-427, J82, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.58×** | +9.7 | 2e-20 | 41/44 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.46×** | +9.2 | 2e-18 | 36/44 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Entrectinib (drug)]] 5 µM |  | **2.21×** | +8.1 | 3e-14 | 38/44 (HOP62, A498, …) | top dose only | position effect removed |
| [[Posaconazole (drug)]] 5 µM |  | **2.00×** | +6.8 | 4e-10 | 33/44 (HEC-1-A, NCI-H1573, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.02×** | +6.7 | 1e-09 | 20/29 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.94×** | +6.5 | 3e-09 | 27/44 (HOP62, HEC-1-A, …) | top dose only | plate-row cell shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +6.5 | 4e-09 | 26/37 (SHP-77, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.91×** | +6.4 | 7e-09 | 31/43 (HOP62, A498, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.90×** | +6.3 | 9e-09 | 31/44 (HOP62, A498, …) | rises with dose | plate-row cell shift |
| [[Berbamine (drug)]] 0.5 µM |  | **1.73×** | +5.6 | 7e-07 | 27/42 (LS 180, HT-29, …) | rises with dose |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.62×** | +4.7 | 7e-05 | 22/44 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.58×** | +4.7 | 8e-05 | 24/44 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | **1.38×** | +4.6 | 1e-04 | 21/44 (HT-29, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +4.4 | 3e-04 | 21/44 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10312.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.676×** | -5.8 | 4e-06 | 25/43 (A-427, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.617×** | -5.0 | 1e-04 | 21/44 (KATO III, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.678×** | -4.1 | 0.009 | 18/42 (RKO, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.688×** | -3.9 | 0.013 | 17/44 (A-427, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.682×** | -3.8 | 0.018 | 18/43 (HCT15, AN3 CA, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.687×** | -3.6 | 0.027 | 16/40 (NCI-H460, A-427, …) | all doses, flat | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.709×** | -3.6 | 0.027 | 16/43 (KATO III, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Quinestrol (drug)]] 5 µM |  | **0.796×** | -3.4 | 0.048 | 15/44 (KATO III, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.798×** | -3.4 | 0.050 | 13/44 (A498, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Hexylresorcinol (drug)]] 5 µM |  | **0.809×** | -3.2 | 0.083 | 10/45 (SW 1088, SNU-1, …) | rises with dose | position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.809×** | -3.2 | 0.083 | 14/44 (PANC-1, HS-578T, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.747× | -3.1 | 0.11 | 11/43 (A498, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10312. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 14.0 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0501× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 10.7 | 2 | 1 (1 ⚠) | [[Cepharanthine (drug)]] 5 µM 4.25× (z +9.4) | [[Nimesulide (drug)]] 5 µM 0.163× (z -8.5) ⚠ toxic; unreliable plate only |
| [[NCI-H23 (line)]] | alt | 7.52 | 2 | 1 (1 ⚠) | [[Cepharanthine (drug)]] 5 µM 6.59× (z +11.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.118× (z -9.0) ⚠ toxic |
| [[A-427 (line)]] | wt | 36.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -14.6) |
| [[A498 (line)]] | wt | 8.29 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.56× (z +8.7) | — |
| [[A549 (line)]] | wt | 4.45 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 8.64× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 15.7 | 2 | 0 | [[Berbamine (drug)]] 5 µM 3.59× (z +11.1) | — |
| [[HOP62 (line)]] | alt | 8.77 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 6.42× (z +12.0) | — |
| [[HS-578T (line)]] | alt | 10.4 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 5.08× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 21.4 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.97× (z +10.8) | — |
| [[LoVo (line)]] | wt | 8.78 | 2 | 0 | [[Berbamine (drug)]] 5 µM 5.27× (z +11.2) | — |
| [[LS 180 (line)]] | wt | 15.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Berbamine (drug)]] 5 µM 3.74× (z +8.9) | — |
| [[SW480 (line)]] | alt | 12.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.12× (z +10.7) | — |
| [[BT-474 (line)]] | alt | 42.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -9.1) |
| [[C32 (line)]] | wt | 9.52 | 0 | 1 | — | [[Rapamycin (drug)]] 0.5 µM 0.0453× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0984× (z -9.0) ⚠ toxic |
| [[HCT15 (line)]] | alt | 16.6 | 0 | 1 | — | [[ULK-101 (drug)]] 0.05 µM 0.0729× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 16.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -8.7) |
| [[A-172 (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10312), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGCR]] | +0.85 | +0.89 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 904 |
| [[MSMO1]] | +0.84 | +0.83 / +0.79 | both halves | 7e-06 | pathway: Cholesterol biosynthesis; STRING 925 |
| [[FDFT1]] | +0.83 | +0.83 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 938 |
| [[SCD]] | +0.81 | +0.87 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 663 |
| [[DHCR24]] | +0.80 | +0.80 / +0.76 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MTORC1_SIGNALING; STRING 996 |
| [[CYP51A1]] | +0.80 | +0.82 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 978 |
| [[HMGCS1]] | +0.79 | +0.79 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 947 |
| [[FASN]] | +0.78 | +0.83 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 757 |
| [[IDI1]] | +0.78 | +0.79 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 864 |
| [[SC5D]] | +0.77 | +0.75 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 998 |
| [[PCSK9]] | +0.76 | +0.78 / +0.75 | both halves | 7e-06 | STRING 421 |
| [[ACSS2]] | +0.76 | +0.75 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 457 |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF830]] | -0.46 | -0.28 / -0.48 | both halves | 3e-04 |  |
| [[ZNF721]] | -0.43 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[ALKBH1]] | -0.42 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[ANKRD17-DT]] | -0.42 | -0.34 / -0.31 | both halves | 2e-04 |  |
| [[MTG2]] | -0.42 | -0.32 / -0.34 | both halves | 2e-04 |  |
| [[MAILR]] | -0.41 | -0.32 / -0.26 | both halves | 3e-04 |  |
| [[XPC]] | -0.41 | -0.34 / -0.34 | both halves | 1e-04 |  |
| [[ANKRD26]] | -0.41 | -0.37 / -0.28 | both halves | 3e-04 |  |
| [[SCGB2B2]] | -0.41 | -0.26 / -0.37 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[QPRT]] | B | QPRT activity raises DHCR7's level | lines that do not express QPRT (21) vs lines expressing it (29) | 1.33× lower at baseline in the lines without QPRT | 0.084 | ⚠ within organs, on part of the lines; also absent: OPRD1, FREM2, SERPINF1 |
| [[KIF1A]] | B | KIF1A activity raises DHCR7's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 1.44× lower at baseline in the lines without KIF1A | 0.089 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Topotecan (hydrochloride) (drug)]] 0.5 µM | C | DHCR7, [[ENSG00000254682]] activity raises the cells' numbers under Topotecan (hydrochloride) 0.5 µM (protects the cells) | lines that do not express DHCR7, ENSG00000254682 (3) vs lines expressing them (45) | the lines without DHCR7, ENSG00000254682: 0.71× the cells of the other lines | 0.071 | ⚠ few lines (3 vs 47); across organs; also absent: LPIN3, TACC2, INSR; co-absent genes |
| cells under [[Anethole trithione (drug)]] 5 µM | C | DHCR7, [[ENSG00000254682]] activity lowers the cells' numbers under Anethole trithione 5 µM (makes them more sensitive) | lines that do not express DHCR7, ENSG00000254682 (3) vs lines expressing them (45) | the lines without DHCR7, ENSG00000254682: 1.18× the cells of the other lines | 0.084 | ⚠ few lines (3 vs 47); across organs; also absent: LPIN3, TACC2, INSR; co-absent genes |
| cells under [[Belinostat (drug)]] 5 µM | C | DHCR7, [[ENSG00000254682]] activity raises the cells' numbers under Belinostat 5 µM (protects the cells) | lines that do not express DHCR7, ENSG00000254682 (3) vs lines expressing them (45) | the lines without DHCR7, ENSG00000254682: 0.65× the cells of the other lines | 0.097 | ⚠ few lines (3 vs 47); across organs; also absent: LPIN3, TACC2, INSR; co-absent genes |

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.924). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.1, -49.1); signed map (-52.6, 32.2). **Vector** length 128, 36.5% of its response variance represented; |z| ≥ 3 in 1,207 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Lanosterol biosynthesis* (reactome, mean cos +0.74 to 10); *Zymostenol biosynthesis via lathosterol (Kandutsch-Russell pathway)* (reactome, mean cos +0.73 to 7); *SREBP1 lipogenesis* (control, mean cos +0.70 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +9.8 | +16.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.7 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.6 | +11.7 |
|  | [[Berbamine (drug)]] 5 µM |  | +8.1 | +16.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.7 | +6.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +5.3 | +8.1 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +4.6 | +6.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.2 | +4.0 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.6 | -3.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -3.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.3 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.2 | -4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.4 | -5.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | 7-dehydrocholesterol reductase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:71,428,193-71,452,868 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SLOS |
| Gene groups (HGNC) | AEBS complex subunits; Dehydrocholesterol reductases |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, ESTROGEN_RESPONSE_LATE, ADIPOGENESIS, ESTROGEN_RESPONSE_EARLY, MTORC1_SIGNALING |
| Reactome | 7 pathways, smallest: Cholesterol biosynthesis from zymosterol (modified Kandutsch-Russell pathway); Cholesterol biosynthesis via desmosterol (Bloch pathway); Cholesterol biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBM7](https://www.uniprot.org/uniprotkb/Q9UBM7) (7-dehydrocholesterol reductase):

> Oxidoreductase that catalyzes the last step of the cholesterol synthesis pathway, which transforms cholesta-5,7-dien-3beta-ol (7-dehydrocholesterol,7-DHC) into cholesterol by reducing the C7-C8 double bond of its sterol core. Can also metabolize cholesta-5,7,24-trien-3beta-ol (7-dehydrodemosterol, 7-DHD) to desmosterol, which is then metabolized by the Delta(24)-sterol reductase (DHCR24) to cholesterol (By similarity). Modulates ferroptosis (a form of regulated cell death driven by …

**Summary**, from NCBI Gene [1717](https://www.ncbi.nlm.nih.gov/gene/1717):

> This gene encodes an enzyme that removes the C(7-8) double bond in the B ring of sterols and catalyzes the conversion of 7-dehydrocholesterol to cholesterol. This gene is ubiquitously expressed and its transmembrane protein localizes to the endoplasmic reticulum membrane and nuclear outer membrane. Mutations in this gene cause Smith-Lemli-Opitz syndrome (SLOS); a syndrome that is metabolically characterized by reduced serum cholesterol levels and elevated serum 7-dehydrocholesterol levels and …

**Accessions** — [HGNC:2860](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2860) · Entrez [1717](https://www.ncbi.nlm.nih.gov/gene/1717) · UniProt [Q9UBM7](https://www.uniprot.org/uniprotkb/Q9UBM7) · Ensembl [ENSG00000172893](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172893)

## Data

Gene col 10312: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10312); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10312, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10312]; `tensor/DDL_lfc|DDL_z.npy` [10312]; `embed/gene_vectors.npy` [10312]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10312 or target_col == 10312). Every well: [[DHCR7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHCR7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
