---
symbol: "ALKBH2"
type: "gene"
col: 12080
ensembl_id: "ENSG00000189046"
name: "alkB homolog 2, alpha-ketoglutarate dependent dioxygenase"
location: "12q24.11"
module: 33
arm: "+"
pooled_cpm: 6.78
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# ALKBH2

*alkB homolog 2, alpha-ketoglutarate dependent dioxygenase* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.54× (z +11.5, q 5e-28, up in 35 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Glycyrrhizic acid (drug)]] 0.5 µM: 0.735× (z -3.8, q 0.069, down in 14 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM in 1 line (A498 0.0431×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SHP-77 0.0844×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (A549 0.0618×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EMSLR]] (+0.74, fdr 7e-06), [[NLE1]] (+0.71, fdr 7e-06), [[UTP14A]] (+0.70, fdr 7e-06); moves opposite to [[GNAS]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12080.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.54×** | +11.5 | 5e-28 | 35/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.43×** | +11.0 | 1e-25 | 23/29 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.48×** | +10.8 | 6e-25 | 7/10 (LOX-IMVI, A498, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.28×** | +10.2 | 3e-22 | 30/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.93×** | +7.5 | 6e-12 | 12/17 (AsPC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.74×** | +6.8 | 8e-10 | 25/46 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +6.6 | 3e-09 | 17/31 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.63×** | +6.1 | 1e-07 | 22/47 (Hs 766T, NCI-H460, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +5.5 | 3e-06 | 9/29 (LoVo, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.51×** | +5.1 | 2e-05 | 18/45 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.46×** | +4.7 | 1e-04 | 11/47 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +4.5 | 3e-04 | 10/47 (NCI-H1792, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.41×** | +4.2 | 0.001 | 10/46 (LOX-IMVI, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.2 | 0.001 | 18/40 (LOX-IMVI, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.42×** | +4.2 | 0.001 | 20/44 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.004 | 13/47 (SK-MEL-2, SHP-77, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.016 | 11/47 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.022 | 12/44 (SK-MEL-2, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.68×** | +3.3 | 0.022 | 3/37 (SW480, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.022 | 7/46 (C32, PANC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.63×** | +3.1 | 0.041 | 3/39 (MIA PaCa-2, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.60×** | +3.1 | 0.053 | 1/43 (NCI-H1573) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.60×** | +3.0 | 0.055 | 5/39 (AsPC-1, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.05 µM |  | **1.27×** | +3.0 | 0.063 | 3/46 (H4, SW480, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.50×** | +2.9 | 0.078 | 4/32 (SNU-423, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12080.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM in 1 line (A498 0.0431×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SHP-77 0.0844×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (A549 0.0618×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.735×** | -3.8 | 0.069 | 14/45 (RPMI-7951, SK-MEL-2, …) | inconsistent across doses | low cells (technical?) |
| [[Bergenin (drug)]] 5 µM |  | 0.825× | -3.4 | 0.16 | 13/46 (BT-474, Hs 766T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.765× | -3.3 | 0.16 | 13/47 (BT-474, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12080. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 12.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 4.72 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM 0.0431× (z -14.1) |
| [[A549 (line)]] | wt | 7.32 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0618× (z -11.8) |
| [[HS-578T (line)]] | alt | 4.53 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -9.2) ⚠ cell-cycle shift, explains ~44% of this change |
| [[NCI-H460 (line)]] | wt | 4.52 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.5× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SHP-77 (line)]] | alt | 12.1 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0844× (z -12.0) |
| [[SNU-423 (line)]] | alt | 3.29 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0680× (z -8.5) |
| [[A-172 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12080), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMSLR]] | +0.74 | +0.69 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[NLE1]] | +0.71 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[UTP14A]] | +0.70 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[BCS1L]] | +0.69 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[NUFIP1]] | +0.69 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[BYSL]] | +0.68 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[RITA1]] | +0.68 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[IMP4]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[DDX31]] | +0.67 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[NDUFAF4]] | +0.67 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[EXOSC2]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[POLR1B]] | +0.65 | +0.52 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.57 | -0.43 / -0.59 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.717). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-15.2, -40.5); signed map (-3.3, -44.9). **Vector** length 57.9, 8.35% of its response variance represented; |z| ≥ 3 in 842 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.50 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.50 to 10); *rRNA processing* (reactome, mean cos +0.50 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.1 | +6.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.6 | +11.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +1.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.8 | +3.1 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -0.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.2 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -3.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -1.5 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.3 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.3 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -1.7 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | alkB homolog 2, alpha-ketoglutarate dependent dioxygenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:109,088,188-109,093,631 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC90512, ABH2 |
| Gene groups (HGNC) | Alkylation repair homologs |
| Reactome | 3 pathways, smallest: Reversal of alkylation damage by DNA dioxygenases; DNA Damage Reversal; DNA Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NS38](https://www.uniprot.org/uniprotkb/Q6NS38) (DNA oxidative demethylase ALKBH2):

> Dioxygenase that repairs alkylated nucleic acid bases by direct reversal oxidative dealkylation. Can process both double-stranded (ds) and single-stranded (ss) DNA substrates, with a strong preference for dsDNA. Uses molecular oxygen, 2-oxoglutarate and iron as cofactors to oxidize the alkyl groups that are subsequently released as aldehydes, regenerating the undamaged bases. Probes the base pair stability, locates a weakened base pair and flips the damaged base to accommodate the lesion in its …

**Summary**, from NCBI Gene [121642](https://www.ncbi.nlm.nih.gov/gene/121642):

> The Escherichia coli AlkB protein protects against the cytotoxicity of methylating agents by repair of the specific DNA lesions generated in single-stranded DNA. ALKBH2 and ALKBH3 (MIM 610603) are E. coli AlkB homologs that catalyze the removal of 1-methyladenine and 3-methylcytosine (Duncan et al., 2002 [PubMed 12486230]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:32487](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32487) · Entrez [121642](https://www.ncbi.nlm.nih.gov/gene/121642) · UniProt [Q6NS38](https://www.uniprot.org/uniprotkb/Q6NS38) · Ensembl [ENSG00000189046](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189046)

## Data

Gene col 12080: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12080); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12080, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12080]; `tensor/DDL_lfc|DDL_z.npy` [12080]; `embed/gene_vectors.npy` [12080]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12080 or target_col == 12080). Every well: [[ALKBH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALKBH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
