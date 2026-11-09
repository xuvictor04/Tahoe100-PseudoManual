---
symbol: "CXCL5"
type: "gene"
col: 8767
ensembl_id: "ENSG00000163735"
name: "C-X-C motif chemokine ligand 5"
location: "4q13.3"
module: 14
arm: "+"
pooled_cpm: 22.17
n_lines_expressing: 15
n_dd_up: 34
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 9
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# CXCL5

*C-X-C motif chemokine ligand 5* — 4q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.80× (z +13.4, q 2e-38, up in 11 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.14× (z +11.4, q 1e-27, up in 9 of 12 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (KATO III 0.0602×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 1 line (KATO III 0.0634×; ⚠ cell-cycle shift, explains ~0% of this change); [[Belinostat (drug)]] 5 µM in 1 line (KATO III 0.0848×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CXCL1]] (+0.68, fdr 7e-06), [[CXCL3]] (+0.61, fdr 1e-05, ⚠ same locus), [[CXCL2]] (+0.57, fdr 1e-05), [[SLC44A3-AS1]] (+0.56, fdr 3e-05); moves opposite to [[ZNF568]] (-0.50, fdr 1e-04), [[ZNF404]] (-0.48, fdr 3e-05), [[ZNF439]] (-0.47, fdr 1e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 9 go from it, the strongest it → [[SLIT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 16 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8767.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.80×** | +13.4 | 2e-38 | 11/12 (HOP62, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.14×** | +11.4 | 1e-27 | 9/12 (HOP62, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.38×** | +11.4 | 1e-27 | 9/10 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.01×** | +10.5 | 2e-23 | 10/11 (HOP62, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.81×** | +9.4 | 7e-19 | 12/12 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **3.50×** | +8.8 | 1e-16 | 13/13 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.42×** | +8.3 | 8e-15 | 10/12 (Panc 03.27, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.26×** | +8.1 | 4e-14 | 11/12 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.65×** | +6.9 | 4e-10 | 12/12 (KATO III, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.98×** | +6.8 | 5e-10 | 7/13 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.67×** | +5.1 | 1e-05 | 9/13 (NCI-H1792, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **2.12×** | +5.1 | 2e-05 | 10/12 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.97×** | +4.8 | 8e-05 | 8/13 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +4.7 | 1e-04 | 8/12 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.94×** | +4.7 | 1e-04 | 12/13 (KATO III, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.6 | 2e-04 | 9/12 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +4.5 | 3e-04 | 5/12 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.87×** | +4.4 | 3e-04 | 11/12 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.015 | 5/12 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.53×** | +3.0 | 0.056 | 7/13 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +3.0 | 0.056 | 7/13 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.82×** | +3.0 | 0.057 | 3/12 (MIA PaCa-2, NCI-H460, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **1.35×** | +3.0 | 0.057 | 1/13 (NCI-H1792) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.059 | 5/13 (NCI-H1792, MIA PaCa-2, …) | top dose only |  |
| [[palbociclib (drug)]] 0.05 µM |  | **1.55×** | +2.9 | 0.063 | 3/12 (NCI-H460, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (KATO III 0.0602×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 1 line (KATO III 0.0634×; ⚠ cell-cycle shift, explains ~0% of this change); [[Belinostat (drug)]] 5 µM in 1 line (KATO III 0.0848×; ⚠ cell-cycle shift, explains ~0% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8767. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 93.4 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 6.83× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.0602× (z -14.8) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 72.0 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.84× (z +10.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 4.76× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 125 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 4.87× (z +9.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 4.17× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 10.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 26.0× (z +17.6) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.59× (z +10.2) | — |
| [[A549 (line)]] | wt | 186 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.96× (z +9.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 6.65× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 81.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.25× (z +14.7) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 5.00× (z +11.2) | — |
| [[hTERT-HPNE (line)]] | wt | 10.6 | 3 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 8.02× (z +9.7) | — |
| [[Panc 03.27 (line)]] | alt | 15.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.67× (z +12.0) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 6.78× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 16.9 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 11.6× (z +9.9) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 4.14× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 166 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.22× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 5.77 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +10.9) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[SW 900 (line)]] | alt | 6.07 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 10.6× (z +9.0) | — |
| [[A-172 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.14 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.29 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8767), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CXCL1]] | +0.68 | +0.62 / +0.66 | both halves | 7e-06 | same gene group; pathway: Chemokine receptors bind chemokines; STRING 999 |
| [[CXCL3]] | +0.61 | +0.52 / +0.57 | both halves | 1e-05 | same gene group; pathway: Chemokine receptors bind chemokines; STRING 999; ⚠ same locus (37.9 kb, same strand: neighbours can correlate without regulation) |
| [[CXCL2]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 | same gene group; pathway: Chemokine receptors bind chemokines; STRING 998 |
| [[SLC44A3-AS1]] | +0.56 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[STEAP2-AS1]] | +0.53 | +0.44 / +0.32 | both halves | 2e-04 |  |
| [[EYA4]] | +0.53 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[CXCL8]] | +0.51 | +0.51 / +0.57 | both halves | 1e-05 | same gene group; pathway: Chemokine receptors bind chemokines; STRING 951 |
| [[NKX3-1]] | +0.51 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[FGF2]] | +0.50 | +0.47 / +0.44 | both halves | 3e-05 | STRING 455 |
| [[HNF4G]] | +0.50 | +0.47 / +0.34 | both halves | 1e-04 |  |
| [[LINC02605]] | +0.50 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[TNFSF15]] | +0.50 | +0.43 / +0.35 | both halves | 1e-04 |  |
| [[CDH2]] | +0.49 | +0.52 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF568]] | -0.50 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[ZNF404]] | -0.48 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[ZNF439]] | -0.47 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[MAPK8IP3]] | -0.46 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[WASF2]] | -0.46 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[PPIL2]] | -0.45 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[SLC25A42]] | -0.44 | -0.27 / -0.33 | both halves | 3e-04 |  |
| [[NPRL2]] | -0.44 | -0.40 / -0.30 | both halves | 2e-04 |  |
| [[FAM156A]] | -0.44 | -0.20 / -0.49 | both halves | 7e-04 |  |
| [[WDR37]] | -0.43 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[SLC27A1]] | -0.43 | -0.40 / -0.25 | both halves | 4e-04 |  |
| [[RANBP10]] | -0.43 | -0.39 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CXCL5's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[CXCL3]] | B | CXCL3 activity raises CXCL5's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 2.52× lower at baseline in the lines without CXCL3 | 0.069 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[CXCL8]] | B | CXCL8 activity raises CXCL5's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 2.33× lower at baseline in the lines without CXCL8 | 0.092 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |
| [[QPCT]] | C | QPCT activity raises CXCL5's level | lines that do not express QPCT (25) vs lines expressing it (25) | 2.56× lower at baseline in the lines without QPCT | 0.017 | ⚠ within organs, on part of the lines; also absent: WFDC10B, LRRN1, KRT81; co-absent with the target |
| [[TNFAIP2]] | C | TNFAIP2 activity raises CXCL5's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 3.52× lower at baseline in the lines without TNFAIP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLIT2]] | B | CXCL5 activity raises SLIT2's level | lines that do not express CXCL5 (35) vs lines expressing it (15) | 2.32× lower at baseline in the lines without CXCL5 | 0.019 | ⚠ within organs, on part of the lines; also absent: ANXA10, IRAK3, TRBC2 |
| [[CXCL3]] | B | CXCL5 activity raises CXCL3's level | lines that do not express CXCL5 (35) vs lines expressing it (15) | 2.39× lower at baseline in the lines without CXCL5 | 0.027 | ⚠ within organs, on part of the lines; also absent: ANXA10, IRAK3, TRBC2 |
| [[CXCL8]] | B | CXCL5 activity raises CXCL8's level | lines that do not express CXCL5 (35) vs lines expressing it (15) | 3.07× lower at baseline in the lines without CXCL5 | 0.029 | ⚠ within organs, on part of the lines; also absent: ANXA10, IRAK3, TRBC2 |
| [[PKP4]] | B | CXCL5 activity strengthens PKP4's drug response | lines that do not express CXCL5 (35) vs lines expressing it (14) | the lines without CXCL5 respond 0.78× as strongly (z diff +0.94); strongest at Homoharringtonine 5 µM: 1.22x vs 1.87x (z diff +5.7) | 0.033 | ⚠ within organs, on part of the lines; also absent: ANXA10, IRAK3, TRBC2; target measured in part of the lines; both ways; artifact flags |
| [[CXCL1]] | B | CXCL5 activity raises CXCL1's level | lines that do not express CXCL5 (35) vs lines expressing it (15) | 2.98× lower at baseline in the lines without CXCL5 | 0.038 | ⚠ within organs, on part of the lines; also absent: ANXA10, IRAK3, TRBC2 |
| [[TNFAIP2]] | C | CXCL5 activity raises TNFAIP2's level | lines that do not express CXCL5 (35) vs lines expressing it (15) | 2.83× lower at baseline in the lines without CXCL5 | 0.008 | ⚠ within organs, on part of the lines; also absent: ANXA10, IRAK3, TRBC2; co-absent with the target |
| [[QPCT]] | C | CXCL5 activity raises QPCT's level | lines that do not express CXCL5 (35) vs lines expressing it (15) | 2.11× lower at baseline in the lines without CXCL5 | 0.025 | ⚠ within organs, on part of the lines; also absent: ANXA10, IRAK3, TRBC2; co-absent with the target |
| [[VCAM1]] | C | CXCL5 activity raises VCAM1's level | lines that do not express CXCL5 (35) vs lines expressing it (15) | 1.47× lower at baseline in the lines without CXCL5 | 0.044 | ⚠ within organs, on part of the lines; also absent: ANXA10, IRAK3, TRBC2; co-absent with the target |
| [[PTX3]] | C | CXCL5 activity raises PTX3's level | lines that do not express CXCL5 (35) vs lines expressing it (15) | 2.52× lower at baseline in the lines without CXCL5 | 0.046 | ⚠ within organs, on part of the lines; also absent: ANXA10, IRAK3, TRBC2; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.326). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.2, 6.0); signed map (41.8, 7.5). **Vector** length 57.1, 18.8% of its response variance represented; |z| ≥ 3 in 501 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +13.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +10.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +1.0 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -2.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.9 | -1.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -0.9 | -2.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -0.9 | +0.3 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -0.8 | -0.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -0.8 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | C-X-C motif chemokine ligand 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.3 — chr4:73,995,642-73,998,677 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ENA-78; previously SCYB5 |
| Gene groups (HGNC) | Chemokine ligands |
| Reactome | 7 pathways, smallest: Chemokine receptors bind chemokines; Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [P42830](https://www.uniprot.org/uniprotkb/P42830) (C-X-C motif chemokine 5):

> Involved in neutrophil activation. In vitro, ENA-78(8-78) and ENA-78(9-78) show a threefold higher chemotactic activity for neutrophil granulocytes.

**Summary**, from NCBI Gene [6374](https://www.ncbi.nlm.nih.gov/gene/6374):

> This gene encodes a protein that is a member of the CXC subfamily of chemokines. Chemokines, which recruit and activate leukocytes, are classified by function (inflammatory or homeostatic) or by structure. This protein is proposed to bind the G-protein coupled receptor chemokine (C-X-C motif) receptor 2 to recruit neutrophils, to promote angiogenesis and to remodel connective tissues. This protein is thought to play a role in cancer cell proliferation, migration, and invasion. [provided by …

**Accessions** — [HGNC:10642](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10642) · Entrez [6374](https://www.ncbi.nlm.nih.gov/gene/6374) · UniProt [P42830](https://www.uniprot.org/uniprotkb/P42830) · Ensembl [ENSG00000163735](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163735)

## Data

Gene col 8767: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8767); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8767, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8767]; `tensor/DDL_lfc|DDL_z.npy` [8767]; `embed/gene_vectors.npy` [8767]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8767 or target_col == 8767). Every well: [[CXCL5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CXCL5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
