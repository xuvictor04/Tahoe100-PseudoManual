---
symbol: "CACNG8"
type: "gene"
col: 6620
ensembl_id: "ENSG00000142408"
name: "calcium voltage-gated channel auxiliary subunit gamma 8"
location: "19q13.42"
module: 101
arm: "+"
pooled_cpm: 41.25
n_lines_expressing: 36
n_dd_up: 5
n_dd_down: 30
n_dd_up_clean: 5
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# CACNG8

*calcium voltage-gated channel auxiliary subunit gamma 8* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.39× (z +5.0, q 3e-04, up in 18 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.335× (z -11.7, q 1e-28, down in 32 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAH17]] (+0.57, fdr 3e-05), [[CCDC71L]] (+0.54, fdr 4e-05), [[CEACAM16-AS1]] (+0.53, fdr 1e-04); moves opposite to [[IARS2]] (-0.57, fdr 2e-05), [[NIPSNAP2]] (-0.53, fdr 3e-05), [[OXA1L]] (-0.51, fdr 5e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CACNG6]] → it (grade C ⚠); 5 go from it, the strongest it → [[C1RL-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6620.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.0 | 3e-04 | 18/34 (SW480, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.48×** | +4.0 | 0.013 | 19/33 (A549, COLO 205, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.47×** | +4.0 | 0.013 | 16/33 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +3.6 | 0.042 | 16/34 (LS 180, C-33 A, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.41×** | +3.5 | 0.052 | 14/33 (A549, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.35× | +3.3 | 0.11 | 16/33 (SW480, NCI-H460, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6620.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.335×** | -11.7 | 1e-28 | 32/34 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.405×** | -9.6 | 2e-19 | 29/33 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.423×** | -9.2 | 9e-18 | 30/33 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.412×** | -9.1 | 1e-17 | 29/32 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.488×** | -7.6 | 3e-12 | 30/33 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.532×** | -6.7 | 2e-09 | 25/34 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.533×** | -6.7 | 2e-09 | 27/34 (NCI-H460, AsPC-1, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.544×** | -6.5 | 6e-09 | 24/33 (NCI-H460, A498, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.550×** | -6.1 | 6e-08 | 22/34 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.567×** | -6.0 | 9e-08 | 21/33 (RPMI-7951, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.569×** | -6.0 | 1e-07 | 22/34 (NCI-H460, A498, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.591×** | -5.6 | 1e-06 | 18/34 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.593×** | -5.6 | 1e-06 | 25/34 (CFPAC-1, NCI-H23, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.370×** | -5.5 | 1e-06 | 26/34 (NCI-H23, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.377×** | -5.4 | 2e-06 | 24/33 (MIA PaCa-2, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.391×** | -5.2 | 6e-06 | 24/33 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here); noisy plate (z scaled); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.647×** | -4.6 | 1e-04 | 24/34 (AsPC-1, A498, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.665×** | -4.1 | 0.001 | 20/34 (NCI-H1792, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.537×** | -3.5 | 0.014 | 12/34 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.795×** | -3.4 | 0.016 | 15/34 (CFPAC-1, Panc 03.27, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6620. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 40.0 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -18.0) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.154× (z -14.3) |
| [[MIA PaCa-2 (line)]] | alt | 84.7 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.120× (z -12.4) ⚠ toxic; cell-cycle shift, explains ~44% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 25.7 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 73.2 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.159× (z -14.8) |
| [[AsPC-1 (line)]] | alt | 32.9 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.169× (z -10.6) |
| [[A549 (line)]] | wt | 94.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -11.4) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.215× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 56.7 | 0 | 4 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -13.5) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0709× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 51.9 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.173× (z -10.3) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.186× (z -10.2) |
| [[A498 (line)]] | wt | 76.7 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.262× (z -9.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[CFPAC-1 (line)]] | alt | 44.7 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.357× (z -10.6) |
| [[Hs 766T (line)]] | wt | 32.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.175× (z -9.5) |
| [[LoVo (line)]] | wt | 16.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 104 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.321× (z -8.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Panc 03.27 (line)]] | alt | 25.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.182× (z -9.9) |
| [[SW480 (line)]] | alt | 10.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +10.5) | — |
| [[A-172 (line)]] | wt | 94.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.189× (z -11.7) ⚠ toxic |
| [[A-427 (line)]] | wt | 55.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0937× (z -10.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 78.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.167× (z -10.6) |
| [[LS 180 (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -9.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 190 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.15× (z +10.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-423 (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.191× (z -9.3) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 7.64 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.70 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.52 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.85 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.31 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.61 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.21 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.51 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.61 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.78 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6620), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAH17]] | +0.57 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[CCDC71L]] | +0.54 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[CEACAM16-AS1]] | +0.53 | +0.34 / +0.55 | both halves | 1e-04 |  |
| [[MDGA1]] | +0.53 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[HCG20]] | +0.53 | +0.31 / +0.58 | both halves | 2e-04 |  |
| [[CLCF1]] | +0.52 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[LUCAT1]] | +0.52 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[PPEF1]] | +0.52 | +0.43 / +0.39 | both halves | 5e-05 |  |
| [[SERPINB9]] | +0.52 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[SP140]] | +0.52 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[GNG4]] | +0.52 | +0.37 / +0.55 | both halves | 8e-05 | pathway: Neuronal System |
| [[CYP27C1]] | +0.52 | +0.49 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IARS2]] | -0.57 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[NIPSNAP2]] | -0.53 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[OXA1L]] | -0.51 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[ATP5F1C]] | -0.50 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[LNPK]] | -0.47 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[MANEA]] | -0.47 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[LONP2]] | -0.47 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[HADH]] | -0.47 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[IFT172]] | -0.46 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[CCNG1]] | -0.46 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[CDCA7L]] | -0.45 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[SAMM50]] | -0.45 | -0.38 / -0.45 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNG6]] | C | CACNG6 activity raises CACNG8's level | lines that do not express CACNG6 (18) vs lines expressing it (32) | 4.06× lower at baseline in the lines without CACNG6 | 0.010 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, RAB31, CYP27C1; co-absent with the target |
| [[CYP27C1]] | C | CYP27C1 activity raises CACNG8's level | lines that do not express CYP27C1 (19) vs lines expressing it (31) | 2.95× lower at baseline in the lines without CYP27C1 | 0.049 | ⚠ within organs, on part of the lines; also absent: CACNG6, ENSG00000289526, RAB31; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1RL-AS1]] | B | CACNG8 activity strengthens C1RL-AS1's drug response | lines that do not express CACNG8 (10) vs lines expressing it (31) | the lines without CACNG8 respond 0.64× as strongly (z diff +1.82); strongest at Digitoxin 5 µM: 0.72x vs 0.29x (z diff +4.6) | 0.029 | ⚠ within organs, on part of the lines; also absent: CACNG6, GAB3, KHDC1; target measured in part of the lines; artifact flags |
| [[HMGN2P46]] | B | CACNG8 activity raises HMGN2P46's level | lines that do not express CACNG8 (14) vs lines expressing it (36) | 2.44× lower at baseline in the lines without CACNG8 | 0.042 | ⚠ within organs, on part of the lines; also absent: CACNG6, GAB3, KHDC1 |
| [[MIR22HG]] | B | CACNG8 activity raises MIR22HG's level | lines that do not express CACNG8 (14) vs lines expressing it (36) | 1.40× lower at baseline in the lines without CACNG8 | 0.067 | ⚠ within organs, on part of the lines; also absent: CACNG6, GAB3, KHDC1 |
| [[C1RL-AS1]] | B | CACNG8 activity raises C1RL-AS1's level | lines that do not express CACNG8 (14) vs lines expressing it (36) | 2.12× lower at baseline in the lines without CACNG8 | 0.075 | ⚠ within organs, on part of the lines; also absent: CACNG6, GAB3, KHDC1 |
| [[MOB3C]] | B | CACNG8 activity strengthens MOB3C's drug response | lines that do not express CACNG8 (14) vs lines expressing it (33) | the lines without CACNG8 respond 0.64× as strongly (z diff +0.67); strongest at Panobinostat 0.05 µM: 0.87x vs 0.57x (z diff +1.4) | 0.076 | ⚠ within organs, on part of the lines; also absent: CACNG6, GAB3, KHDC1; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.643). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.7, -2.6); signed map (2.2, 31.1). **Vector** length 90.8, 25.9% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +4.9 | -3.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.8 | -1.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.8 | +1.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +1.3 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -4.0 | -4.6 |
|  | [[NG25 (drug)]] 5 µM |  | -3.6 | -5.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -2.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.9 | -1.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.7 | -2.2 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | calcium voltage-gated channel auxiliary subunit gamma 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:53,962,937-53,990,215 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Calcium channel auxiliary gamma subunits; MicroRNA protein coding host genes |
| Reactome | 10 pathways, smallest: LGI-ADAM interactions; Phase 2 - plateau phase; Phase 0 - rapid depolarisation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXS5](https://www.uniprot.org/uniprotkb/Q8WXS5) (Voltage-dependent calcium channel gamma-8 subunit):

> Regulates the activity of L-type calcium channels that contain CACNA1C as pore-forming subunit (By similarity). Regulates the trafficking and gating properties of AMPA-selective glutamate receptors (AMPARs). Promotes their targeting to the cell membrane and synapses and modulates their gating properties by slowing their rates of activation, deactivation and desensitization and by mediating their resensitization. Does not show subunit-specific AMPA receptor regulation and regulates all AMPAR …

**Summary**, from NCBI Gene [59283](https://www.ncbi.nlm.nih.gov/gene/59283):

> The protein encoded by this gene is a type I transmembrane AMPA receptor regulatory protein (TARP). TARPs regulate both trafficking and channel gating of the AMPA receptors. This gene is part of a functionally diverse eight-member protein subfamily of the PMP-22/EMP/MP20 family and is located in a cluster with two family members, a type II TARP and a calcium channel gamma subunit. The mRNA for this gene is believed to initiate translation from a non-AUG (CUG) start codon. [provided by RefSeq, …

**Accessions** — [HGNC:13628](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13628) · Entrez [59283](https://www.ncbi.nlm.nih.gov/gene/59283) · UniProt [Q8WXS5](https://www.uniprot.org/uniprotkb/Q8WXS5) · Ensembl [ENSG00000142408](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142408)

## Data

Gene col 6620: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6620); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6620, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6620]; `tensor/DDL_lfc|DDL_z.npy` [6620]; `embed/gene_vectors.npy` [6620]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6620 or target_col == 6620). Every well: [[CACNG8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CACNG8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
