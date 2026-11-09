---
symbol: "HCN3"
type: "gene"
col: 6783
ensembl_id: "ENSG00000143630"
name: "hyperpolarization activated cyclic nucleotide gated potassium channel 3"
location: "1q22"
module: 157
arm: "+"
pooled_cpm: 3.18
n_lines_expressing: 49
n_dd_up: 29
n_dd_down: 5
n_dd_up_clean: 21
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# HCN3

*hyperpolarization activated cyclic nucleotide gated potassium channel 3* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.94× (z +9.5, q 1e-18, up in 19 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.596× (z -5.3, q 7e-05, down in 14 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDR1]] (+0.66, fdr 7e-06), [[CDH24]] (+0.61, fdr 7e-06), [[IL11RA]] (+0.58, fdr 1e-05); moves opposite to [[METTL2B]] (-0.55, fdr 4e-05), [[EIF2B3]] (-0.51, fdr 3e-05), [[PRKAG1]] (-0.50, fdr 3e-05).
> It is in [[Module 157]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TRPM2-AS]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6783.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +9.5 | 1e-18 | 19/32 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.87×** | +9.0 | 5e-17 | 15/42 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +7.3 | 4e-11 | 2/2 (A498, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.02×** | +7.2 | 1e-10 | 16/43 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +6.6 | 6e-09 | 11/30 (J82, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +6.3 | 3e-08 | 11/28 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +5.9 | 3e-07 | 13/40 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.73×** | +5.6 | 2e-06 | 6/18 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.72×** | +5.5 | 2e-06 | 14/40 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.62×** | +4.7 | 2e-04 | 9/35 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.56×** | +4.5 | 3e-04 | 2/18 (HEC-1-A, C-33 A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +4.3 | 1e-03 | 1/7 (HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.55×** | +4.1 | 0.002 | 4/27 (HEC-1-A, Hs 766T, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.005 | 7/35 (NCI-H23, SW480, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +3.7 | 0.007 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.30×** | +3.7 | 0.007 | 7/39 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +3.7 | 0.008 | 8/43 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.011 | 6/40 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +3.5 | 0.012 | 11/34 (J82, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.017 | 5/30 (HCT15, A498, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6783.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.596×** | -5.3 | 7e-05 | 14/32 (NCI-H23, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Naproxen (drug)]] 5 µM |  | **0.673×** | -3.9 | 0.027 | 7/35 (NCI-H1792, HS-578T, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.695×** | -3.6 | 0.052 | 4/43 (SW48, NCI-H2347, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.709×** | -3.5 | 0.052 | 12/39 (HEC-1-A, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.696×** | -3.5 | 0.052 | 10/36 (Hs 766T, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ritonavir (drug)]] 0.05 µM |  | 0.731× | -3.2 | 0.13 | 5/41 (RKO, NCI-H460, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.740× | -3.1 | 0.16 | 4/41 (NCI-H2030, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6783. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.04 | 0 | 3 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0877× (z -10.3) ⚠ toxic; unreliable plate only · without an alert: [[Monocrotaline (drug)]] 0.05 µM 0.101× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 4.00 | 0 | 2 | — | [[Tetracycline (hydrochloride) (drug)]] 0.05 µM 0.0512× (z -10.0) |
| [[COLO 205 (line)]] | alt | 5.20 | 0 | 1 | — | [[Ranolazine (drug)]] 0.05 µM 0.0550× (z -9.1) |
| [[KATO III (line)]] | alt | 3.73 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0709× (z -8.8) |
| [[A-427 (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.649 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.811 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.917 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6783), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDR1]] | +0.66 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[CDH24]] | +0.61 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[IL11RA]] | +0.58 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ZNF775]] | +0.55 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[GET4]] | +0.55 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[MTMR11]] | +0.55 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[BMF]] | +0.53 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[SLC9A3-AS1]] | +0.53 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[MAPK3]] | +0.53 | +0.39 / +0.58 | both halves | 5e-05 | pathway: Neuronal System |
| [[DVL2]] | +0.53 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[RARG]] | +0.51 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[PRRT2]] | +0.51 | +0.51 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL2B]] | -0.55 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[EIF2B3]] | -0.51 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[PRKAG1]] | -0.50 | -0.49 / -0.45 | both halves | 3e-05 | pathway: Neuronal System |
| [[DAP3]] | -0.48 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[HLCS]] | -0.45 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[UTP11]] | -0.45 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[RRP7BP-1]] | -0.45 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[MTHFD2L]] | -0.44 | -0.32 / -0.54 | both halves | 1e-04 |  |
| [[EIF3J]] | -0.44 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[TAS2R14]] | -0.44 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[LDLRAD3]] | -0.44 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[CCT6A]] | -0.43 | -0.43 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRPM2-AS]] | B | TRPM2-AS activity raises HCN3's level | lines that do not express TRPM2-AS (29) vs lines expressing it (21) | 1.38× lower at baseline in the lines without TRPM2-AS | 0.050 | ⚠ within organs, on part of the lines; also absent: LINC03046, KLRC2, PCK1 |
| [[PSMB5]] | B | PSMB5 activity raises HCN3's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MUC1]] | B | MUC1 activity raises HCN3's level | lines that do not express MUC1 (25) vs lines expressing it (25) | 1.47× lower at baseline in the lines without MUC1 | 0.097 | ⚠ within organs, on part of the lines; also absent: TACSTD2, UCA1, RNF223 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.582). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.5, -23.3); signed map (0.1, 6.1). **Vector** length 46.7, 5.75% of its response variance represented; |z| ≥ 3 in 879 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +4.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.4 | +4.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.8 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +1.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +3.8 |
| fall | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.2 | -5.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.2 | -3.5 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.2 | -0.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | hyperpolarization activated cyclic nucleotide gated potassium channel 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:155,277,463-155,289,848 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1535 |
| Gene groups (HGNC) | Cyclic nucleotide gated channels |
| Reactome | 3 pathways, smallest: HCN channels; Potassium Channels; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P1Z3](https://www.uniprot.org/uniprotkb/Q9P1Z3) (Potassium/sodium hyperpolarization-activated cyclic nucleotide-gated channel 3):

> Hyperpolarization-activated ion channel that are permeable to sodium and potassium ions, with an about 3:1 preference for potassium ions. Contributes to the native pacemaker currents in heart (If) and in neurons (Ih). In particular, plays a pivotal role in maintaining excitability and promoting rhythmic burst firing within hypothalamic nuclei. Exerts a significant influence on the configuration of the cardiac action potential waveform. Does not appear to play a prominent role in the processing …

**Summary**, from NCBI Gene [57657](https://www.ncbi.nlm.nih.gov/gene/57657):

> This gene encodes a multi-pass membrane protein that functions as a voltage gated cation channel. The encoded protein is a member of a family of closely related cyclic adenosine monophosphate-binding channel proteins. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:19183](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19183) · Entrez [57657](https://www.ncbi.nlm.nih.gov/gene/57657) · UniProt [Q9P1Z3](https://www.uniprot.org/uniprotkb/Q9P1Z3) · Ensembl [ENSG00000143630](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143630)

## Data

Gene col 6783: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6783); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6783, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6783]; `tensor/DDL_lfc|DDL_z.npy` [6783]; `embed/gene_vectors.npy` [6783]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6783 or target_col == 6783). Every well: [[HCN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HCN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
