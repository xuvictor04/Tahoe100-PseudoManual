---
symbol: "SEL1L"
type: "gene"
col: 985
ensembl_id: "ENSG00000071537"
name: "SEL1L adaptor subunit of SYVN1 ubiquitin ligase"
location: "14q31"
module: 42
arm: "+"
pooled_cpm: 131.98
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# SEL1L

*SEL1L adaptor subunit of SYVN1 ubiquitin ligase* — 14q31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.04× (z +12.4, q 9e-33, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.377× (z -16.4, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSPA5]] (+0.82, fdr 7e-06), [[HYOU1]] (+0.80, fdr 7e-06), [[TMED2]] (+0.77, fdr 7e-06); moves opposite to [[TRIM47]] (-0.57, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); 2 go from it, the strongest it → [[RSL24D1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 985.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.04×** | +12.4 | 9e-33 | 45/48 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.99×** | +12.0 | 8e-31 | 46/48 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.73×** | +9.5 | 3e-19 | 44/48 (A549, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +5.7 | 2e-06 | 36/48 (LOX-IMVI, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 985.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.377×** | -16.4 | 0e+00 | 47/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.551×** | -12.3 | 2e-32 | 39/48 (A-172, J82, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.494×** | -12.3 | 2e-32 | 46/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.569×** | -9.4 | 5e-19 | 40/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.628×** | -8.1 | 6e-14 | 39/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.659×** | -7.3 | 3e-11 | 39/48 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.680×** | -6.7 | 1e-09 | 35/48 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.689×** | -6.5 | 6e-09 | 39/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.737×** | -4.9 | 5e-05 | 34/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.809×** | -3.7 | 0.013 | 23/48 (PANC-1, KATO III, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.841× | -3.6 | 0.015 | 23/48 (SW48, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.823×** | -3.4 | 0.032 | 22/48 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.824×** | -3.1 | 0.081 | 20/45 (SK-MEL-2, SW480, …) | inconsistent across doses | composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.841× | -3.0 | 0.098 | 18/48 (HT-29, LS 180, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.842× | -3.0 | 0.098 | 20/49 (HT-29, LS 180, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.842× | -3.0 | 0.098 | 16/48 (H4, A549, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 985. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 103 | 3 | 5 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.03× (z +13.4) | [[Harringtonine (drug)]] 5 µM 0.308× (z -13.8) |
| [[A498 (line)]] | wt | 88.5 | 3 | 4 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.86× (z +13.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.371× (z -12.8) |
| [[AsPC-1 (line)]] | alt | 96.0 | 2 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.17× (z +8.7) | [[Harringtonine (drug)]] 5 µM 0.271× (z -14.1) |
| [[J82 (line)]] | alt | 86.7 | 2 | 5 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.31× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -15.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.280× (z -13.9) |
| [[PANC-1 (line)]] | alt | 101 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.306× (z -17.1) |
| [[A-172 (line)]] | wt | 95.2 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.129× (z -21.9) |
| [[HS-578T (line)]] | alt | 134 | 1 | 4 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.28× (z +8.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.339× (z -11.8) |
| [[HT-29 (line)]] | alt | 203 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.226× (z -11.3) |
| [[KATO III (line)]] | alt | 332 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.190× (z -13.1) |
| [[SW480 (line)]] | alt | 126 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.55× (z +12.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.454× (z -10.0) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 76.1 | 4 | 0 | [[Auranofin (drug)]] 5 µM 2.51× (z +10.7) | — |
| [[NCI-H2347 (line)]] | alt | 177 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.319× (z -13.9) |
| [[NCI-H460 (line)]] | wt | 118 | 1 | 3 | [[Panobinostat (drug)]] 5 µM 2.58× (z +10.8) | [[Harringtonine (drug)]] 5 µM 0.447× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 237 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.243× (z -15.6) |
| [[H4 (line)]] | wt | 214 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.266× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 96.4 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.48× (z +8.6) | [[Harringtonine (drug)]] 5 µM 0.364× (z -9.3) |
| [[HOP62 (line)]] | alt | 109 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.30× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -8.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[hTERT-HPNE (line)]] | wt | 180 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.356× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 112 | 0 | 3 | — | [[Harringtonine (drug)]] 0.5 µM 0.268× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 148 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.79× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -9.7) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H23 (line)]] | alt | 84.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.12× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.192× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 88.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.79× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 98.9 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.265× (z -15.1) |
| [[SW1417 (line)]] | alt | 121 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.14× (z +9.0) | [[Harringtonine (drug)]] 5 µM 0.454× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 117 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.09× (z +10.0) | — |
| [[LoVo (line)]] | wt | 137 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.219× (z -11.1) |
| [[LS 180 (line)]] | wt | 231 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.184× (z -11.1) |
| [[RPMI-7951 (line)]] | alt | 128 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.327× (z -11.3) |
| [[A-427 (line)]] | wt | 81.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.413× (z -8.9) |
| [[AN3 CA (line)]] | alt | 104 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.254× (z -8.5) |
| [[BT-474 (line)]] | alt | 117 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.77× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 63.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.06× (z +9.6) | — |
| [[C32 (line)]] | wt | 124 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.88× (z +9.8) | — |
| [[HCT15 (line)]] | alt | 144 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.233× (z -9.6) |
| [[Hs 766T (line)]] | wt | 111 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.348× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 165 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 189 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.44× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 151 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.307× (z -14.4) |
| [[SK-MEL-2 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.347× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[SNU-1 (line)]] | wt | 101 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.180× (z -14.4) |
| [[SW 1088 (line)]] | alt | 164 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.108× (z -9.5) |
| [[SW 900 (line)]] | alt | 166 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.397× (z -9.2) |
| [[CHP-212 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 105 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 163 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 985), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPA5]] | +0.82 | +0.83 / +0.78 | both halves | 7e-06 | STRING 949 |
| [[HYOU1]] | +0.80 | +0.81 / +0.82 | both halves | 7e-06 | STRING 854 |
| [[TMED2]] | +0.77 | +0.78 / +0.74 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 412 |
| [[DNAJC3]] | +0.77 | +0.77 / +0.76 | both halves | 7e-06 | STRING 611 |
| [[ERP44]] | +0.76 | +0.69 / +0.73 | both halves | 7e-06 | STRING 402 |
| [[HSP90B1]] | +0.75 | +0.74 / +0.72 | both halves | 7e-06 | STRING 833 |
| [[COPA]] | +0.74 | +0.75 / +0.71 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SEC61A1]] | +0.74 | +0.78 / +0.72 | both halves | 7e-06 | STRING 790 |
| [[PDIA4]] | +0.74 | +0.73 / +0.70 | both halves | 7e-06 | STRING 737 |
| [[GFPT1]] | +0.74 | +0.70 / +0.76 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[LMAN1]] | +0.72 | +0.68 / +0.69 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 401 |
| [[SLC31A1]] | +0.71 | +0.69 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM47]] | -0.57 | -0.53 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers SEL1L's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RSL24D1]] | C | SEL1L's natural level weakens RSL24D1's drug response | SEL1L's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.65, reverse +0.36; direction not clear | 0.038 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ERP44]] | C | SEL1L's natural level weakens ERP44's drug response | SEL1L's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse -0.08; direction not clear | 0.074 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.818). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.2, -30.7); signed map (-54.7, 7.7). **Vector** length 146, 50.2% of its response variance represented; |z| ≥ 3 in 1,086 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Maturation of DENV proteins* (reactome, mean cos +0.67 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.67 to 12); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.51 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +8.2 | +12.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.2 | +5.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.9 | +12.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.1 | +9.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.1 | +2.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.1 | +2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.0 | +2.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.8 | +2.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -11.0 | -16.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.9 | -12.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.4 | -9.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -8.2 | -12.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.2 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.9 | -6.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.8 | -4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -3.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | SEL1L adaptor subunit of SYVN1 ubiquitin ligase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q31 — chr14:81,471,547-81,533,853 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IBD2, SEL1L1, Hrd3 |
| Reactome | 23 pathways, smallest: Pre-NOTCH Processing in Golgi; ER Quality Control Compartment (ERQC); Calnexin/calreticulin cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBV2](https://www.uniprot.org/uniprotkb/Q9UBV2) (Protein sel-1 homolog 1):

> Plays a role in the endoplasmic reticulum quality control (ERQC) system also called ER-associated degradation (ERAD) involved in ubiquitin-dependent degradation of misfolded endoplasmic reticulum proteins. Enhances SYVN1 stability. Plays a role in LPL maturation and secretion. Required for normal differentiation of the pancreas epithelium, and for normal exocrine function and survival of pancreatic cells. May play a role in Notch signaling.

**Summary**, from NCBI Gene [6400](https://www.ncbi.nlm.nih.gov/gene/6400):

> The protein encoded by this gene is part of a protein complex required for the retrotranslocation or dislocation of misfolded proteins from the endoplasmic reticulum lumen to the cytosol, where they are degraded by the proteasome in a ubiquitin-dependent manner. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:10717](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10717) · Entrez [6400](https://www.ncbi.nlm.nih.gov/gene/6400) · UniProt [Q9UBV2](https://www.uniprot.org/uniprotkb/Q9UBV2) · Ensembl [ENSG00000071537](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071537)

## Data

Gene col 985: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 985); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 985, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 985]; `tensor/DDL_lfc|DDL_z.npy` [985]; `embed/gene_vectors.npy` [985]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 985 or target_col == 985). Every well: [[SEL1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEL1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
