---
symbol: "CHPF"
type: "gene"
col: 4469
ensembl_id: "ENSG00000123989"
name: "chondroitin polymerizing factor"
location: "2q35"
module: 42
arm: "+"
pooled_cpm: 21.61
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 19
n_dd_up_clean: 2
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# CHPF

*chondroitin polymerizing factor* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.28× (z +10.4, q 9e-23, up in 32 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 1.46× (z +4.8, q 1e-04, up in 19 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A498 2.78×, AsPC-1 3.89×, NCI-H1573 4.69×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (HEC-1-A 4.76×, SW1417 3.04×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.451× (z -10.1, q 3e-21, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMED9]] (+0.66, fdr 7e-06), [[GLT8D1]] (+0.66, fdr 9e-06), [[TRAPPC1]] (+0.65, fdr 1e-05); moves opposite to [[CPEB1]] (-0.57, fdr 3e-05), [[TYW3]] (-0.54, fdr 3e-05), [[GABPB2]] (-0.53, fdr 8e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4469.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A498 2.78×, AsPC-1 3.89×, NCI-H1573 4.69×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (HEC-1-A 4.76×, SW1417 3.04×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.28×** | +10.4 | 9e-23 | 32/38 (A498, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.82×** | +7.3 | 1e-10 | 22/29 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.66×** | +6.4 | 2e-08 | 29/44 (SW480, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.53×** | +5.4 | 9e-06 | 26/47 (LOX-IMVI, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.47×** | +4.9 | 1e-04 | 22/47 (SNU-423, A-172, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.46×** | +4.8 | 1e-04 | 19/47 (HOP62, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.45×** | +4.7 | 2e-04 | 21/47 (LOX-IMVI, SNU-423, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **1.37×** | +3.7 | 0.014 | 16/35 (NCI-H2030, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.019 | 19/47 (HOP62, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.30×** | +3.4 | 0.046 | 14/45 (HEC-1-A, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4469.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.451×** | -10.1 | 3e-21 | 35/47 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.606×** | -9.0 | 7e-17 | 33/46 (HS-578T, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.482×** | -8.9 | 1e-16 | 36/46 (HepG2/C3A, A549, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.530×** | -8.1 | 8e-14 | 30/45 (HS-578T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.517×** | -8.1 | 8e-14 | 27/46 (HS-578T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.537×** | -7.9 | 3e-13 | 37/47 (KATO III, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.549×** | -7.6 | 2e-12 | 31/47 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.589×** | -6.7 | 1e-09 | 28/46 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.599×** | -6.5 | 5e-09 | 30/47 (A-172, C32, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.582×** | -6.5 | 5e-09 | 31/45 (A498, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.609×** | -6.3 | 2e-08 | 33/47 (KATO III, HepG2/C3A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.641×** | -5.6 | 8e-07 | 31/46 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.646×** | -5.6 | 1e-06 | 27/46 (HS-578T, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.715×** | -4.3 | 8e-04 | 20/45 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.735×** | -3.9 | 0.003 | 19/47 (C32, HS-578T, …) | top dose only |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.748×** | -3.4 | 0.023 | 10/47 (SW480, NCI-H2347, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4469. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 36.5 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -19.6) |
| [[C32 (line)]] | wt | 115 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -14.8) |
| [[A498 (line)]] | wt | 38.0 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.265× (z -12.8) |
| [[KATO III (line)]] | alt | 34.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -17.6) |
| [[A-172 (line)]] | wt | 40.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.210× (z -13.1) |
| [[H4 (line)]] | wt | 30.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -11.8) |
| [[A549 (line)]] | wt | 7.61 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0518× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 21.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HEC-1-A (line)]] | alt | 12.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.76× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[HepG2_C3A (line)]] | wt | 51.3 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0861× (z -16.0) |
| [[Hs 766T (line)]] | wt | 23.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 28.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 11.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 37.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.173× (z -11.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 43.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.04× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[SW480 (line)]] | alt | 21.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.317× (z -9.8) |
| [[A-427 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.55 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.25 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4469), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED9]] | +0.66 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[GLT8D1]] | +0.66 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[TRAPPC1]] | +0.65 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[FAM234A]] | +0.65 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[RTL8C]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[KDELR3]] | +0.64 | +0.64 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[GGCX]] | +0.63 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[PDIA5]] | +0.63 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[P3H1]] | +0.63 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[C11orf24]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[IDH2]] | +0.62 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[YIPF2]] | +0.62 | +0.59 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPEB1]] | -0.57 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[TYW3]] | -0.54 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[GABPB2]] | -0.53 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[CATSPERE]] | -0.53 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[KCNMB3]] | -0.53 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[RNLS]] | -0.52 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[CCDC122]] | -0.52 | -0.48 / -0.22 | both halves | 6e-04 |  |
| [[GRIP1]] | -0.52 | -0.49 / -0.25 | both halves | 4e-04 |  |
| [[C11orf58]] | -0.51 | -0.32 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CHPF's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.613). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.7, -31.1); signed map (-48.2, 7.2). **Vector** length 89.0, 20.8% of its response variance represented; |z| ≥ 3 in 932 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +3.7 | +5.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +3.3 | +4.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +3.3 | +4.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | -2.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +2.1 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.5 | +4.8 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | +1.5 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.7 | -6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.4 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | -6.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.3 | -7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.5 | -2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | chondroitin polymerizing factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:219,538,954-219,543,809 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CSS2, CHSY2, CHPF1 |
| Gene groups (HGNC) | Beta 4-glycosyltransferases; Beta 3-glycosyltransferases |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 4 pathways, smallest: CS-GAG biosynthesis; Chondroitin sulfate/dermatan sulfate metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZ52](https://www.uniprot.org/uniprotkb/Q8IZ52) (Chondroitin polymerizing factor, non-catalytic subunit):

> Non-catalytic component of CHSY1-CHPF and CHSY3-CHPF chondroitin sulfate synthase complexes. CHPF associates with catalytically active chondroitin synthases (CHSY1/3) within heterodimeric complexes. Plays an essential role for the formation of a stable and functional chondroitin sulfate polymerase complexes.; [Isoform 2]: May facilitate PRKN transport into the mitochondria. In collaboration with PRKN, may enhance cell viability and protect cells from oxidative stress.

**Summary**, from NCBI Gene [79586](https://www.ncbi.nlm.nih.gov/gene/79586):

> Enables N-acetylgalactosaminyl-proteoglycan 3-beta-glucuronosyltransferase activity and glucuronosyl-N-acetylgalactosaminyl-proteoglycan 4-beta-N-acetylgalactosaminyltransferase activity. Involved in chondroitin sulfate proteoglycan biosynthetic process. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24291](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24291) · Entrez [79586](https://www.ncbi.nlm.nih.gov/gene/79586) · UniProt [Q8IZ52](https://www.uniprot.org/uniprotkb/Q8IZ52) · Ensembl [ENSG00000123989](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123989)

## Data

Gene col 4469: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4469); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4469, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4469]; `tensor/DDL_lfc|DDL_z.npy` [4469]; `embed/gene_vectors.npy` [4469]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4469 or target_col == 4469). Every well: [[CHPF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHPF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
