---
symbol: "LRCH4"
type: "gene"
col: 1187
ensembl_id: "ENSG00000077454"
name: "leucine rich repeats and calponin homology domain containing 4"
location: "7q22.1"
module: 138
arm: "+"
pooled_cpm: 11.88
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# LRCH4

*leucine rich repeats and calponin homology domain containing 4* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.65× (z +19.3, q 0e+00, up in 37 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.644× (z -6.1, q 5e-07, down in 23 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H460 0.141×, HS-578T 0.125×, J82 0.131×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (KATO III 0.0945×, NCI-H1573 0.187×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Radotinib (drug)]] 0.5 µM in 2 lines (SW48 0.0757×, HS-578T 0.163×); [[Sulfisoxazole (drug)]] 0.5 µM in 1 line (Hs 766T 0.0778×); [[Hydroxyurea (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0842×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PNPLA2]] (+0.67, fdr 7e-06), [[ABHD16A]] (+0.61, fdr 1e-05), [[EDC4]] (+0.60, fdr 3e-05); moves opposite to [[NAA50]] (-0.53, fdr 7e-05), [[ZNF234]] (-0.53, fdr 6e-05), [[BCCIP]] (-0.52, fdr 3e-05).
> It is in [[Module 138]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[C1orf226]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1187.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.65×** | +19.3 | 0e+00 | 37/44 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.02×** | +9.8 | 2e-20 | 33/48 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.99×** | +9.6 | 1e-19 | 30/47 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.92×** | +9.1 | 1e-17 | 33/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.74×** | +7.3 | 3e-11 | 29/46 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.58×** | +6.4 | 1e-08 | 21/46 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +6.0 | 2e-07 | 22/45 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +5.2 | 2e-05 | 22/45 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +5.0 | 3e-05 | 18/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.37×** | +4.5 | 5e-04 | 17/41 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.003 | 14/47 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.0 | 0.003 | 16/39 (CFPAC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.63×** | +3.6 | 0.016 | 9/42 (AsPC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~14% of this change | **1.28×** | +3.2 | 0.050 | 9/40 (SHP-77, HEC-1-A, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.095 | 5/47 (HEC-1-A, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1187.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H460 0.141×, HS-578T 0.125×, J82 0.131×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (KATO III 0.0945×, NCI-H1573 0.187×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Radotinib (drug)]] 0.5 µM in 2 lines (SW48 0.0757×, HS-578T 0.163×); [[Sulfisoxazole (drug)]] 0.5 µM in 1 line (Hs 766T 0.0778×); [[Hydroxyurea (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0842×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.644×** | -6.1 | 5e-07 | 23/47 (AsPC-1, NCI-H23, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.745×** | -3.8 | 0.034 | 13/45 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.842× | -3.4 | 0.14 | 18/45 (SW480, HT-29, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1187. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 21.0 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[LoVo (line)]] | wt | 16.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +12.0) | — |
| [[NCI-H460 (line)]] | wt | 7.26 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +13.4) | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 11.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +13.1) | — |
| [[HS-578T (line)]] | alt | 8.80 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Radotinib (drug)]] 0.5 µM 0.163× (z -8.7) |
| [[KATO III (line)]] | alt | 16.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0945× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 6.01 | 0 | 1 | — | [[Berberine (chloride hydrate) (drug)]] 0.5 µM 0.127× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 9.35 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 13.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +10.6) | — |
| [[HepG2_C3A (line)]] | wt | 9.45 | 0 | 1 | — | [[crizotinib (drug)]] 0.05 µM 0.102× (z -8.5) |
| [[HOP62 (line)]] | alt | 8.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 9.54 | 0 | 1 | — | [[Sulfisoxazole (drug)]] 0.5 µM 0.0778× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 8.45 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.5 µM 0.0842× (z -9.4) |
| [[J82 (line)]] | alt | 7.62 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 15.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +10.4) | — |
| [[RKO (line)]] | wt | 11.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 5.89 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.105× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 20.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +11.7) | — |
| [[SW48 (line)]] | wt | 15.1 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0757× (z -10.7) |
| [[A-172 (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1187), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNPLA2]] | +0.67 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[ABHD16A]] | +0.61 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[EDC4]] | +0.60 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[MBD6]] | +0.60 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[DGAT1]] | +0.59 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[TAOK2]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[PANK4]] | +0.56 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[SRF]] | +0.56 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[USP19]] | +0.56 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[RXRB]] | +0.56 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[TRIM28]] | +0.55 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[AGRN]] | +0.55 | +0.58 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA50]] | -0.53 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[ZNF234]] | -0.53 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[BCCIP]] | -0.52 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[CDC123]] | -0.51 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[BEND3]] | -0.49 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[RAP1GDS1]] | -0.48 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[PAM]] | -0.48 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[CCT8]] | -0.47 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[MRPS35]] | -0.47 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[WDR12]] | -0.47 | -0.37 / -0.38 | both halves | 9e-05 |  |
| [[EIF3I]] | -0.46 | -0.27 / -0.55 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1orf226]] | B | C1orf226 activity raises LRCH4's level | lines that do not express C1orf226 (14) vs lines expressing it (36) | 1.43× lower at baseline in the lines without C1orf226 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, EPS8L2, EEPD1; maybe low, not absent |
| [[EPHB3]] | B | EPHB3 activity raises LRCH4's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 1.37× lower at baseline in the lines without EPHB3 | 0.073 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.652). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.4, -25.0); signed map (-6.9, 20.1). **Vector** length 74.3, 12.6% of its response variance represented; |z| ≥ 3 in 919 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +19.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.9 | +4.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.8 | +9.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.7 | +9.6 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +2.4 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.3 | +3.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +2.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.7 | +0.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.9 | -6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | -4.5 | -3.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -3.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | +1.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.4 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeats and calponin homology domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,574,011-100,586,129 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously LRN, LRRN1 |
| Gene groups (HGNC) | Leucine rich repeats and calponin homology domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O75427](https://www.uniprot.org/uniprotkb/O75427) (Leucine-rich repeat and calponin homology domain-containing protein 4):

> Accessory protein that regulates signaling by multiple TLRs, acting as a broad-spanning regulator of the innate immune response. In macrophages, binds LPS and promotes proper docking of LPS in lipid raft membrane. May be required for lipid raft maintenance.

**Summary**, from NCBI Gene [4034](https://www.ncbi.nlm.nih.gov/gene/4034):

> This gene encodes a protein that contains leucine-rich repeats (LRR) at its amino terminus and that is known to be involved in ligand binding. The carboxyl terminus may act as a membrane anchor. Identified structural elements suggest that the encoded protein resembles a receptor. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6691](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6691) · Entrez [4034](https://www.ncbi.nlm.nih.gov/gene/4034) · UniProt [O75427](https://www.uniprot.org/uniprotkb/O75427) · Ensembl [ENSG00000077454](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077454)

## Data

Gene col 1187: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1187); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1187, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1187]; `tensor/DDL_lfc|DDL_z.npy` [1187]; `embed/gene_vectors.npy` [1187]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1187 or target_col == 1187). Every well: [[LRCH4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRCH4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
