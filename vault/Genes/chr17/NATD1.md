---
symbol: "NATD1"
type: "gene"
col: 15810
ensembl_id: "ENSG00000274180"
name: "N-acetyltransferase domain containing 1"
location: "17p11.2"
module: 69
arm: "+"
pooled_cpm: 2.55
n_lines_expressing: 48
n_dd_up: 29
n_dd_down: 11
n_dd_up_clean: 23
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# NATD1

*N-acetyltransferase domain containing 1* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 4.06× (z +13.1, q 1e-36, up in 41 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.256× (z -12.8, q 1e-34, down in 38 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.287× (z -6.1, q 3e-07, down in 16 of 27 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PNPLA2]] (+0.63, fdr 7e-06), [[ABTB1]] (+0.63, fdr 3e-04), [[CTDSP2]] (+0.61, fdr 1e-05); moves opposite to [[MTREX]] (-0.56, fdr 2e-04), [[NUP107]] (-0.54, fdr 2e-05), [[KPNB1]] (-0.53, fdr 1e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15810.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **4.06×** | +13.1 | 1e-36 | 41/44 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.96×** | +12.9 | 1e-35 | 43/45 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.24×** | +11.0 | 6e-26 | 40/45 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.22×** | +10.6 | 6e-24 | 21/35 (SW1417, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.38×** | +8.1 | 5e-14 | 32/45 (HOP62, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.37×** | +8.1 | 6e-14 | 19/29 (SW1417, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +7.4 | 1e-11 | 15/33 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.71×** | +7.1 | 7e-11 | 21/43 (KATO III, Hs 766T, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.52×** | +5.6 | 1e-06 | 9/44 (J82, A549, …) | top dose only | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +5.4 | 4e-06 | 9/29 (SW1417, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +5.3 | 5e-06 | 11/29 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.6 | 2e-04 | 11/43 (A549, A-172, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +4.5 | 3e-04 | 0/2 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.4 | 4e-04 | 4/14 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +4.2 | 0.001 | 1/1 (A498) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.55×** | +4.1 | 0.001 | 8/44 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.29×** | +4.1 | 0.002 | 2/37 (A498, NCI-H460) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +3.9 | 0.003 | 6/39 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.004 | 6/42 (A-172, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15810.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.256×** | -12.8 | 1e-34 | 38/45 (KATO III, SW480, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.287×** | -6.1 | 3e-07 | 16/27 (A498, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.362×** | -5.0 | 1e-04 | 14/33 (NCI-H23, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.478×** | -4.9 | 1e-04 | 11/45 (LOX-IMVI, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.388×** | -4.6 | 4e-04 | 11/27 (KATO III, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.389×** | -4.6 | 4e-04 | 10/26 (KATO III, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.633×** | -4.0 | 0.004 | 13/39 (HOP62, LoVo, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.680×** | -3.4 | 0.043 | 6/44 (RKO, A498, …) | inconsistent across doses | position effect removed |
| [[EX229 (drug)]] 0.5 µM |  | **0.601×** | -3.4 | 0.043 | 7/40 (LOX-IMVI, A-172, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.701×** | -3.3 | 0.051 | 15/42 (A-427, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.522×** | -3.2 | 0.077 | 8/38 (C-33 A, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.720× | -3.1 | 0.10 | 8/39 (NCI-H23, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15810. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 6.20 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0933× (z -9.4) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 4.00 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0738× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 6.36 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0623× (z -10.3) |
| [[A-172 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.682 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.43 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15810), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNPLA2]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ABTB1]] | +0.63 | +0.27 / +0.72 | both halves | 3e-04 |  |
| [[CTDSP2]] | +0.61 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ATG2A]] | +0.56 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[HECA]] | +0.56 | +0.29 / +0.55 | both halves | 2e-04 |  |
| [[HDAC5]] | +0.56 | +0.37 / +0.60 | both halves | 9e-05 |  |
| [[BAIAP3]] | +0.55 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[TRIM8]] | +0.55 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[MOB2]] | +0.55 | +0.27 / +0.62 | both halves | 3e-04 |  |
| [[CALCOCO1]] | +0.53 | +0.25 / +0.54 | both halves | 4e-04 |  |
| [[OTUD1]] | +0.53 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[UBALD1]] | +0.53 | +0.41 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTREX]] | -0.56 | -0.29 / -0.62 | both halves | 2e-04 |  |
| [[NUP107]] | -0.54 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[KPNB1]] | -0.53 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[TAS2R14]] | -0.49 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[RBM26]] | -0.49 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[ANAPC10]] | -0.49 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[METTL15]] | -0.48 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[TCERG1]] | -0.47 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[RAD54B]] | -0.47 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[SNRPF]] | -0.46 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[XPO4]] | -0.46 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[PMS1]] | -0.45 | -0.38 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NATD1's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.499). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.7, -44.2); signed map (-19.6, 12.4). **Vector** length 45.8, 5.26% of its response variance represented; |z| ≥ 3 in 1,194 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.7 | +3.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +2.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.8 | +10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +7.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.3 | +3.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.3 | +0.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.9 | -12.8 |
|  | [[EX229 (drug)]] 5 µM |  | -3.0 | -4.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.0 | -6.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.7 | -4.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -5.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.4 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | N-acetyltransferase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:21,238,870-21,253,410 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33894, Gtlf3b; previously C17orf103 |
| Matched by | ensembl_id |

UniProt [Q8N6N6](https://www.uniprot.org/uniprotkb/Q8N6N6) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:30770](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30770) · Entrez [256302](https://www.ncbi.nlm.nih.gov/gene/256302) · UniProt [Q8N6N6](https://www.uniprot.org/uniprotkb/Q8N6N6) · Ensembl [ENSG00000274180](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000274180)

## Data

Gene col 15810: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15810); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15810, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15810]; `tensor/DDL_lfc|DDL_z.npy` [15810]; `embed/gene_vectors.npy` [15810]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15810 or target_col == 15810). Every well: [[NATD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NATD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
