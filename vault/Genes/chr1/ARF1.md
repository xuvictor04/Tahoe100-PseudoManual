---
symbol: "ARF1"
type: "gene"
col: 6798
ensembl_id: "ENSG00000143761"
name: "ARF GTPase 1"
location: "1q42.13"
module: 20
arm: "+"
pooled_cpm: 189.95
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# ARF1

*ARF GTPase 1* — 1q42.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.84× (z +9.6, q 3e-19, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.636× (z -8.0, q 7e-13, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HDLBP]] (+0.73, fdr 7e-06), [[TMED2]] (+0.71, fdr 7e-06), [[TMED7]] (+0.70, fdr 7e-06); moves opposite to [[PPP1R35]] (-0.64, fdr 1e-05, ⚠ PPP1R35 in the vector space only through flagged drug-doses), [[NSUN5P1-1]] (-0.64, fdr 1e-05), [[CROCCP2-1]] (-0.63, fdr 1e-05), [[CELF1]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6798.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.84×** | +9.6 | 3e-19 | 48/49 (COLO 205, hTERT-HPNE, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +8.4 | 1e-14 | 45/49 (NCI-H1792, A549, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.53×** | +7.5 | 1e-11 | 39/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.22×** | +7.3 | 3e-11 | 43/48 (hTERT-HPNE, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +6.5 | 1e-08 | 39/44 (NCI-H460, HT-29, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +6.2 | 4e-08 | 33/45 (HEC-1-A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +5.4 | 5e-06 | 39/48 (NCI-H460, PANC-1, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.004 | 30/48 (C32, BT-474, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.23×** | +3.7 | 0.014 | 25/48 (NCI-H460, LoVo, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.22×** | +3.6 | 0.021 | 24/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.024 | 22/48 (NCI-H460, NCI-H23, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.033 | 29/48 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **1.21×** | +3.4 | 0.035 | 25/48 (SK-MEL-2, SNU-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.19× | +3.1 | 0.076 | 17/49 (SW1417, SHP-77, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6798.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.636×** | -8.0 | 7e-13 | 40/48 (HT-29, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.704×** | -6.2 | 2e-07 | 37/48 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.718×** | -5.8 | 1e-06 | 38/48 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.935× | -4.0 | 0.007 | 1/50 (NCI-H23) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -3.2 | 0.16 | 24/48 (HT-29, LoVo, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.842× | -3.0 | 0.22 | 20/48 (LS 180, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6798. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 183 | 4 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +14.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +9.8) | [[Belinostat (drug)]] 5 µM 0.490× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 196 | 7 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +12.5) | — |
| [[HT-29 (line)]] | alt | 223 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.96× (z +9.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.459× (z -11.0) |
| [[PANC-1 (line)]] | alt | 145 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +10.7) | — |
| [[COLO 205 (line)]] | alt | 219 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.65× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 209 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.96× (z +13.5) ⚠ cell-cycle shift, explains ~74% of this change | [[Panobinostat (drug)]] 5 µM 0.493× (z -8.8) |
| [[A498 (line)]] | wt | 266 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 2.98× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.577× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 223 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.493× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 200 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.23× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 142 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 3.88× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 167 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 293 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.02× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.539× (z -13.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 304 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.473× (z -10.2) |
| [[SW48 (line)]] | wt | 219 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.27× (z +9.1) | — |
| [[A-427 (line)]] | wt | 131 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 162 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +9.7) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 204 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.32× (z +9.4) | — |
| [[C32 (line)]] | wt | 137 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.78× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 172 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 1.94× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 206 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.35× (z +8.9) | — |
| [[KATO III (line)]] | alt | 215 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.470× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 182 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.33× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 136 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.21× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 210 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.285× (z -9.0) |
| [[RKO (line)]] | wt | 176 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.554× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 144 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.06× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 166 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 178 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.177× (z -8.8) |
| [[SW480 (line)]] | alt | 144 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.92× (z +9.5) | — |
| [[A-172 (line)]] | wt | 239 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 138 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 117 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 192 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 203 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 282 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 139 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 238 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 151 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 206 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 187 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6798), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDLBP]] | +0.73 | +0.67 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[TMED2]] | +0.71 | +0.72 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION; STRING 830 |
| [[TMED7]] | +0.70 | +0.68 / +0.85 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 619 |
| [[RPN1]] | +0.69 | +0.63 / +0.73 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[TWF1]] | +0.66 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[TXNDC5]] | +0.65 | +0.57 / +0.71 | both halves | 1e-05 | pathway: Golgi Associated Vesicle Biogenesis; STRING 533 |
| [[BPNT2]] | +0.65 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[AGBL5]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[TLN1]] | +0.64 | +0.56 / +0.68 | both halves | 1e-05 | same gene group |
| [[AP2M1]] | +0.63 | +0.56 / +0.69 | both halves | 1e-05 | pathway: HALLMARK_PI3K_AKT_MTOR_SIGNALING |
| [[ZNF460]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[PAPOLA]] | +0.62 | +0.50 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R35]] ⚠ | -0.64 | -0.50 / -0.65 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NSUN5P1-1]] | -0.64 | -0.54 / -0.68 | both halves | 1e-05 |  |
| [[CROCCP2-1]] | -0.63 | -0.54 / -0.68 | both halves | 1e-05 |  |
| [[CELF1]] | -0.60 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[NSUN5P2-1]] ⚠ | -0.60 | -0.49 / -0.67 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[KRI1]] | -0.55 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[EIF5B]] | -0.55 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[PDCD5]] | -0.55 | -0.34 / -0.65 | both halves | 1e-04 |  |
| [[ZNF593]] | -0.53 | -0.32 / -0.66 | both halves | 2e-04 |  |
| [[YBEY]] | -0.53 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[TIMM13]] | -0.52 | -0.30 / -0.57 | both halves | 2e-04 |  |
| [[MRPL32]] | -0.52 | -0.35 / -0.65 | both halves | 1e-04 |  |
| [[NEMF]] | -0.51 | -0.34 / -0.59 | both halves | 1e-04 |  |
| [[GGT7]] | -0.51 | -0.36 / -0.58 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ARF1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CERS4]] | B | CERS4 activity lowers ARF1's level | lines that do not express CERS4 (17) vs lines expressing it (33) | 1.13× higher at baseline in the lines without CERS4 | 0.089 | ⚠ within organs, on part of the lines; also absent: UPK1A-AS1, PCSK1N, CHST10 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.535). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-24.2, -21.9); signed map (-18.7, -34.2). **Vector** length 116, 41.3% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.3 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | +0.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +7.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | +3.0 | +2.2 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +2.9 | +1.7 |
|  | [[Aliskiren (drug)]] 0.5 µM |  | +2.8 | +2.1 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -4.6 | -2.8 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -4.0 | -2.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -4.0 | +3.7 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -3.8 | -2.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -1.8 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -3.0 | -1.8 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -3.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ARF GTPase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.13 — chr1:228,082,708-228,099,212 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | ARF GTPase family; Receptor ligands; MicroRNA protein coding host genes |
| Hallmark sets | PROTEIN_SECRETION, PI3K_AKT_MTOR_SIGNALING |
| Reactome | 33 pathways, smallest: Glycosphingolipid transport; Nef Mediated CD4 Down-regulation; Synthesis of PIPs at the Golgi membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [P84077](https://www.uniprot.org/uniprotkb/P84077) (ADP-ribosylation factor 1):

> Small GTPase involved in protein trafficking between different compartments. Modulates vesicle budding and uncoating within the Golgi complex. In its GTP-bound form, triggers the recruitment of coatomer proteins to the Golgi membrane. The hydrolysis of ARF1-bound GTP, which is mediated by ARFGAPs proteins, is required for dissociation of coat proteins from Golgi membranes and vesicles. The GTP-bound form interacts with PICK1 to limit PICK1-mediated inhibition of Arp2/3 complex activity; the …

**Summary**, from NCBI Gene [375](https://www.ncbi.nlm.nih.gov/gene/375):

> ADP-ribosylation factor 1 (ARF1) is a member of the human ARF gene family. The family members encode small guanine nucleotide-binding proteins that stimulate the ADP-ribosyltransferase activity of cholera toxin and play a role in vesicular trafficking as activators of phospholipase D. The gene products, including 6 ARF proteins and 11 ARF-like proteins, constitute a family of the RAS superfamily. The ARF proteins are categorized as class I (ARF1, ARF2 and ARF3), class II (ARF4 and ARF5) and …

**Accessions** — [HGNC:652](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:652) · Entrez [375](https://www.ncbi.nlm.nih.gov/gene/375) · UniProt [P84077](https://www.uniprot.org/uniprotkb/P84077) · Ensembl [ENSG00000143761](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143761)

## Data

Gene col 6798: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6798); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6798, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6798]; `tensor/DDL_lfc|DDL_z.npy` [6798]; `embed/gene_vectors.npy` [6798]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6798 or target_col == 6798). Every well: [[ARF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
