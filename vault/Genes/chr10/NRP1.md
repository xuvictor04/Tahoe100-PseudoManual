---
symbol: "NRP1"
type: "gene"
col: 1785
ensembl_id: "ENSG00000099250"
name: "neuropilin 1"
location: "10p11.22"
module: 92
arm: "+"
pooled_cpm: 140.51
n_lines_expressing: 34
n_dd_up: 1
n_dd_down: 33
n_dd_up_clean: 0
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 15
direction_downstream: 11
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# NRP1

*neuropilin 1* — 10p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.35× (z +3.8, q 0.091, up in 13 of 29 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 2.28×, RKO 2.61×); [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 3.00×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-172 3.12×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.180× (z -22.4, q 0e+00, down in 32 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAI14]] (+0.50, fdr 1e-05), [[TOP1]] (+0.50, fdr 6e-05), [[MILR1]] (+0.48, fdr 2e-05); moves opposite to [[KIF13A]] (-0.50, fdr 4e-05), [[RETREG1]] (-0.49, fdr 4e-05), [[PPP1R3C]] (-0.48, fdr 3e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[MILR1]] → it (grade B ⚠); 11 go from it, the strongest it → [[ETV6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1785.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 2.28×, RKO 2.61×); [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 3.00×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-172 3.12×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +3.8 | 0.091 | 13/29 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.30× | +3.4 | 0.13 | 13/32 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 1.29× | +3.3 | 0.13 | 14/32 (RPMI-7951, hTERT-HPNE, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.29× | +3.3 | 0.13 | 14/32 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 1.35× | +3.1 | 0.26 | 8/32 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1785.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.180×** | -22.4 | 0e+00 | 32/32 (Panc 03.27, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.303×** | -22.0 | 0e+00 | 30/32 (RPMI-7951, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.207×** | -20.6 | 0e+00 | 32/32 (Panc 03.27, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.245×** | -18.4 | 0e+00 | 31/32 (Panc 03.27, SW 900, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.441×** | -10.1 | 8e-22 | 27/32 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.493×** | -9.2 | 3e-18 | 24/32 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.530×** | -8.3 | 9e-15 | 26/32 (RPMI-7951, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.547×** | -7.9 | 3e-13 | 27/32 (Panc 03.27, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.656×** | -7.8 | 5e-13 | 25/32 (SW 900, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.579×** | -6.9 | 4e-10 | 22/32 (SW 900, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.614×** | -6.1 | 5e-08 | 24/31 (SW 900, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.619×** | -6.0 | 8e-08 | 21/31 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.424×** | -5.9 | 2e-07 | 26/33 (Panc 03.27, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.662×** | -5.4 | 3e-06 | 21/32 (SHP-77, LS 180, …) | top dose only | cell-cycle shift (explains ~24% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.752×** | -5.3 | 6e-06 | 19/33 (A-172, RPMI-7951, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.679×** | -5.0 | 2e-05 | 22/32 (PANC-1, SW 900, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.680×** | -5.0 | 2e-05 | 24/33 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1785. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 601 | 0 | 16 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -24.4) |
| [[RPMI-7951 (line)]] | alt | 741 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0941× (z -28.9) |
| [[HOP62 (line)]] | alt | 158 | 0 | 9 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.472× (z -18.2) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.139× (z -13.9) |
| [[PANC-1 (line)]] | alt | 94.0 | 0 | 9 | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -23.2) |
| [[A498 (line)]] | wt | 277 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0816× (z -17.8) |
| [[Panc 03.27 (line)]] | alt | 279 | 0 | 8 | — | [[Panobinostat (drug)]] 5 µM 0.0713× (z -26.3) |
| [[HS-578T (line)]] | alt | 362 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.0797× (z -20.8) |
| [[LS 180 (line)]] | wt | 62.3 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.207× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 568 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0808× (z -23.3) |
| [[SHP-77 (line)]] | alt | 161 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -19.8) |
| [[A-172 (line)]] | wt | 124 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 3.00× (z +9.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.182× (z -15.0) |
| [[CFPAC-1 (line)]] | alt | 366 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.137× (z -18.8) |
| [[A549 (line)]] | wt | 257 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -15.2) |
| [[KATO III (line)]] | alt | 71.2 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.170× (z -15.0) |
| [[NCI-H2347 (line)]] | alt | 175 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.197× (z -15.2) |
| [[SNU-423 (line)]] | alt | 251 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.113× (z -17.6) |
| [[SW1417 (line)]] | alt | 224 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.146× (z -17.7) |
| [[AsPC-1 (line)]] | alt | 107 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -14.8) |
| [[CHP-212 (line)]] | wt | 283 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -13.4) |
| [[COLO 205 (line)]] | alt | 71.0 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.135× (z -12.9) |
| [[HT-29 (line)]] | alt | 52.4 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.205× (z -13.4) |
| [[J82 (line)]] | alt | 113 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.175× (z -15.9) |
| [[LoVo (line)]] | wt | 47.4 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.253× (z -13.2) |
| [[BT-474 (line)]] | alt | 134 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -14.3) |
| [[LOX-IMVI (line)]] | wt | 130 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.235× (z -10.3) |
| [[RKO (line)]] | wt | 55.5 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -11.6) |
| [[SW480 (line)]] | alt | 53.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -14.8) |
| [[H4 (line)]] | wt | 73.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -12.1) |
| [[hTERT-HPNE (line)]] | wt | 237 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.181× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 150 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -17.5) |
| [[SW 1088 (line)]] | alt | 299 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.110× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 117 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -16.5) |
| [[A-427 (line)]] | wt | 7.79 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 17.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 20.2 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 32.9 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 31.0 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 24.6 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 27.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 30.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 95.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 19.1 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 13.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1785), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAI14]] | +0.50 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[TOP1]] | +0.50 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[MILR1]] | +0.48 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[ITGA3]] | +0.48 | +0.50 / +0.55 | both halves | 1e-05 | same gene group |
| [[MIR100HG]] | +0.48 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[SLC37A2]] | +0.48 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[PRKCA]] | +0.48 | +0.49 / +0.39 | both halves | 5e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[SHC3]] | +0.47 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[RGS17]] | +0.47 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[EDNRA]] | +0.47 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[NID1]] | +0.46 | +0.37 / +0.44 | both halves | 8e-05 |  |
| [[LAMA4]] | +0.46 | +0.46 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF13A]] | -0.50 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[RETREG1]] | -0.49 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[PPP1R3C]] | -0.48 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[DIPK1A]] | -0.47 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[ACBD4]] | -0.47 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[WDSUB1]] | -0.46 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[CRYZL1]] | -0.45 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[TMEM74B]] | -0.45 | -0.40 / -0.26 | both halves | 3e-04 |  |
| [[EXD2]] | -0.45 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[VPS37D]] | -0.45 | -0.32 / -0.36 | both halves | 1e-04 |  |
| [[CC2D1A]] | -0.45 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[HSDL1]] | -0.45 | -0.32 / -0.53 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 14, C 1. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MILR1]] | B | MILR1 activity raises NRP1's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 3.63× lower at baseline in the lines without MILR1 | 0.001 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[GLIS3]] | B | GLIS3 activity raises NRP1's level | lines that do not express GLIS3 (21) vs lines expressing it (29) | 3.48× lower at baseline in the lines without GLIS3 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO |
| [[ADAMTS12]] | B | ADAMTS12 activity raises NRP1's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 4.42× lower at baseline in the lines without ADAMTS12 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1 |
| [[ME3]] | B | ME3 activity raises NRP1's level | lines that do not express ME3 (13) vs lines expressing it (37) | 2.84× lower at baseline in the lines without ME3 | 0.009 | ⚠ within organs, on part of the lines; also absent: PLAAT3 |
| [[WNT5A]] | B | WNT5A activity raises NRP1's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 3.56× lower at baseline in the lines without WNT5A | 0.018 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13 |
| [[TGM2]] | B | TGM2 activity raises NRP1's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 3.72× lower at baseline in the lines without TGM2 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3 |
| [[ITGA11]] | B | ITGA11 activity raises NRP1's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 3.64× lower at baseline in the lines without ITGA11 | 0.048 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411 |
| [[KLKP1-1]] | B | KLKP1-1 activity raises NRP1's level | lines that do not express KLKP1-1 (11) vs lines expressing it (39) | 4.25× lower at baseline in the lines without KLKP1-1 | 0.051 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, ENSG00000286263, MILR1; maybe low, not absent |
| [[ADAMTS9-AS2]] | B | ADAMTS9-AS2 activity raises NRP1's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 3.14× lower at baseline in the lines without ADAMTS9-AS2 | 0.052 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2 |
| [[ITGB3]] | B | ITGB3 activity raises NRP1's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 3.26× lower at baseline in the lines without ITGB3 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[TBX15]] | B | TBX15 activity raises NRP1's level | lines that do not express TBX15 (7) vs lines expressing it (43) | 2.05× lower at baseline in the lines without TBX15 | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[RGS17]] | B | RGS17 activity raises NRP1's level | lines that do not express RGS17 (15) vs lines expressing it (35) | 2.76× lower at baseline in the lines without RGS17 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CFAP20DC, AFAP1L1 |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ETV6]] | B | NRP1 activity raises ETV6's level | lines that do not express NRP1 (16) vs lines expressing it (34) | 1.77× lower at baseline in the lines without NRP1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: BDKRB2, MX2, FAM107B |
| [[GLIS3]] | B | NRP1 activity raises GLIS3's level | lines that do not express NRP1 (16) vs lines expressing it (34) | 3.49× lower at baseline in the lines without NRP1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: BDKRB2, MX2, FAM107B |
| [[CRYZL1]] | B | NRP1 activity lowers CRYZL1's level | lines that do not express NRP1 (16) vs lines expressing it (34) | 1.28× higher at baseline in the lines without NRP1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: BDKRB2, MX2, FAM107B |
| [[KLKP1-1]] | B | NRP1 activity raises KLKP1-1's level | lines that do not express NRP1 (16) vs lines expressing it (34) | 1.83× lower at baseline in the lines without NRP1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: BDKRB2, MX2, FAM107B |
| [[ME3]] | B | NRP1 activity raises ME3's level | lines that do not express NRP1 (16) vs lines expressing it (34) | 1.83× lower at baseline in the lines without NRP1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: BDKRB2, MX2, FAM107B |
| [[TBXAS1]] | B | NRP1 activity raises TBXAS1's level | lines that do not express NRP1 (16) vs lines expressing it (34) | 2.04× lower at baseline in the lines without NRP1 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: BDKRB2, MX2, FAM107B |
| [[FPGT]] | B | NRP1 activity lowers FPGT's level | lines that do not express NRP1 (16) vs lines expressing it (34) | 1.30× higher at baseline in the lines without NRP1 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: BDKRB2, MX2, FAM107B |
| [[RGS17]] | B | NRP1 activity raises RGS17's level | lines that do not express NRP1 (16) vs lines expressing it (34) | 2.06× lower at baseline in the lines without NRP1 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: BDKRB2, MX2, FAM107B |
| [[VCAN]] | B | NRP1 activity raises VCAN's level | lines that do not express NRP1 (16) vs lines expressing it (34) | 2.61× lower at baseline in the lines without NRP1 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: BDKRB2, MX2, FAM107B |
| [[CAB39]] | B | NRP1 activity raises CAB39's level | lines that do not express NRP1 (16) vs lines expressing it (34) | 1.42× lower at baseline in the lines without NRP1 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: BDKRB2, MX2, FAM107B |
| [[EDNRA]] | C | NRP1 activity raises EDNRA's level | lines that do not express NRP1 (16) vs lines expressing it (34) | 2.28× lower at baseline in the lines without NRP1 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: BDKRB2, MX2, FAM107B; co-absent with the target |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.433). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (53.4, 8.0); signed map (12.9, 49.8). **Vector** length 116, 36.7% of its response variance represented; |z| ≥ 3 in 1,245 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.2 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.6 | +2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | -4.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | -0.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.4 | +1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | -1.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | +1.6 |
| fall | [[Trametinib (drug)]] 5 µM |  | -4.8 | -4.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.3 | -3.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.8 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.7 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.7 | -5.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | neuropilin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p11.22 — chr10:33,177,492-33,336,262 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NRP, VEGF165R, CD304 |
| Gene groups (HGNC) | CD molecules; Neuropilin family |
| Hallmark sets | ANGIOGENESIS, HEDGEHOG_SIGNALING, UV_RESPONSE_DN, KRAS_SIGNALING_UP, IL2_STAT5_SIGNALING |
| Reactome | 18 pathways, smallest: Neuropilin interactions with VEGF and VEGFR; CHL1 interactions; SEMA3A-Plexin repulsion signaling by inhibiting Integrin adhesion |
| Matched by | ensembl_id |

**Function**, from UniProt [O14786](https://www.uniprot.org/uniprotkb/O14786) (Neuropilin-1):

> Cell-surface receptor involved in the development of the cardiovascular system, in angiogenesis, in the formation of certain neuronal circuits and in organogenesis outside the nervous system. Mediates the chemorepulsant activity of semaphorins. Recognizes a C-end rule (CendR) motif R/KXXR/K on its ligands which causes cellular internalization and vascular leakage. It binds to semaphorin 3A, the PLGF-2 isoform of PGF, the VEGF165 isoform of VEGFA and VEGFB. Coexpression with KDR results in …

**Summary**, from NCBI Gene [8829](https://www.ncbi.nlm.nih.gov/gene/8829):

> This gene encodes one of two neuropilins, which contain specific protein domains which allow them to participate in several different types of signaling pathways that control cell migration. Neuropilins contain a large N-terminal extracellular domain, made up of complement-binding, coagulation factor V/VIII, and meprin domains. These proteins also contains a short membrane-spanning domain and a small cytoplasmic domain. Neuropilins bind many ligands and various types of co-receptors; they …

**Accessions** — [HGNC:8004](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8004) · Entrez [8829](https://www.ncbi.nlm.nih.gov/gene/8829) · UniProt [O14786](https://www.uniprot.org/uniprotkb/O14786) · Ensembl [ENSG00000099250](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099250)

## Data

Gene col 1785: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1785); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1785, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1785]; `tensor/DDL_lfc|DDL_z.npy` [1785]; `embed/gene_vectors.npy` [1785]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1785 or target_col == 1785). Every well: [[NRP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
