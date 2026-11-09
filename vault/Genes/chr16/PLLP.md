---
symbol: "PLLP"
type: "gene"
col: 2293
ensembl_id: "ENSG00000102934"
name: "plasmolipin"
location: "16q13"
module: 115
arm: "+"
pooled_cpm: 5.26
n_lines_expressing: 46
n_dd_up: 17
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# PLLP

*plasmolipin* — 16q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.11× (z +11.0, q 2e-25, up in 26 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.563× (z -6.0, q 1e-06, down in 20 of 43 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CBLC]] (+0.60, fdr 2e-05), [[PDE9A]] (+0.58, fdr 1e-05), [[ABHD6]] (+0.57, fdr 4e-05); moves opposite to [[NEK11]] (-0.48, fdr 5e-05), [[IRAK4]] (-0.48, fdr 3e-04), [[GANC]] (-0.48, fdr 6e-04).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PIWIL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2293.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.11×** | +11.0 | 2e-25 | 26/40 (NCI-H460, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.96×** | +7.0 | 6e-10 | 5/19 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +5.8 | 1e-06 | 1/6 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +5.1 | 3e-05 | 15/33 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +5.1 | 3e-05 | 16/41 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +4.9 | 1e-04 | 15/40 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +4.5 | 6e-04 | 9/39 (NCI-H2347, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.4 | 9e-04 | 10/28 (HOP62, A549, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +4.3 | 0.001 | 3/18 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.49×** | +4.2 | 0.002 | 8/31 (KATO III, HepG2/C3A, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +3.9 | 0.006 | 1/15 (HEC-1-A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +3.6 | 0.013 | 12/39 (HT-29, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.59×** | +3.5 | 0.022 | 1/24 (PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +3.5 | 0.022 | 10/41 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.042 | 4/37 (CFPAC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.53×** | +3.2 | 0.050 | 1/31 (SW48) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2293.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.563×** | -6.0 | 1e-06 | 20/43 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.585×** | -5.6 | 7e-06 | 14/40 (SNU-1, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.623×** | -4.9 | 2e-04 | 19/41 (A498, SNU-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.665×** | -4.2 | 0.003 | 13/38 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.704×** | -3.7 | 0.030 | 17/37 (SW480, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.707×** | -3.6 | 0.030 | 13/29 (SW480, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.724×** | -3.3 | 0.066 | 11/35 (SNU-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.743× | -3.1 | 0.15 | 7/40 (SK-MEL-2, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2293. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 55.0 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0546× (z -17.4) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0382× (z -13.8) |
| [[NCI-H2030 (line)]] | alt | 27.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -16.0) ⚠ cell-cycle shift, explains ~5% of this change |
| [[SW480 (line)]] | alt | 11.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.180× (z -10.8) |
| [[A-172 (line)]] | wt | 2.33 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.69× (z +8.8) ⚠ cell-cycle shift, explains ~5% of this change | — |
| [[A498 (line)]] | wt | 3.82 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.156× (z -8.5) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 10.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.198× (z -8.9) |
| [[LS 180 (line)]] | wt | 11.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -11.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2293), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBLC]] | +0.60 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[PDE9A]] | +0.58 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[ABHD6]] | +0.57 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[PRKCQ]] | +0.56 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[PIWIL1]] | +0.56 | +0.59 / +0.38 | both halves | 7e-05 |  |
| [[SEMA6B]] | +0.56 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[FCHO1]] | +0.55 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[SOX13]] | +0.55 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[SEMA4D]] | +0.55 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[SGSM1]] | +0.55 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[RASAL1]] | +0.54 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[TGFBR3]] | +0.54 | +0.47 / +0.56 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEK11]] | -0.48 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[IRAK4]] | -0.48 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[GANC]] | -0.48 | -0.22 / -0.48 | both halves | 6e-04 |  |
| [[HTATIP2]] | -0.47 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[ATXN1L]] | -0.47 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[DESI1]] | -0.47 | -0.23 / -0.49 | both halves | 5e-04 |  |
| [[SPAG16]] | -0.46 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[C17orf80]] | -0.46 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[CLIP1]] | -0.46 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[DPH3]] | -0.46 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[STX16]] | -0.46 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[DCTN2]] | -0.45 | -0.39 / -0.46 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIWIL1]] | B | PIWIL1 activity raises PLLP's level | lines that do not express PIWIL1 (38) vs lines expressing it (12) | 2.35× lower at baseline in the lines without PIWIL1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, CALB1, CLRN3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.588). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.3, 47.9); signed map (6.3, 37.0). **Vector** length 55.6, 8.50% of its response variance represented; |z| ≥ 3 in 872 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +11.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +5.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.2 | +4.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.8 | +5.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.6 | +4.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +3.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.0 | +3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.9 | +1.7 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -2.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.7 | -1.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.6 | -1.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | plasmolipin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q13 — chr16:57,248,547-57,284,672 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PMLP; previously TM4SF11 |
| Gene groups (HGNC) | Tetraspan junctional complex superfamily; MARVEL domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y342](https://www.uniprot.org/uniprotkb/Q9Y342) (Plasmolipin):

> Main component of the myelin sheath that plays an important role in myelin membrane biogenesis and myelination. Plays an essential function in apical endocytosis. Regulates epithelial development through the regulation of apical endocytosis (By similarity). Part of the intracellular machinery that mediates basolateral-to-apical transport of ICAM-1, an essential adhesion receptor in epithelial cells, from the subapical compartment in hepatic epithelial cells.

**Summary**, from NCBI Gene [51090](https://www.ncbi.nlm.nih.gov/gene/51090):

> Enables identical protein binding activity. Involved in myelin assembly and regulation of transcytosis. Located in myelin sheath and plasma membrane. Biomarker of schizophrenia. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18553](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18553) · Entrez [51090](https://www.ncbi.nlm.nih.gov/gene/51090) · UniProt [Q9Y342](https://www.uniprot.org/uniprotkb/Q9Y342) · Ensembl [ENSG00000102934](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102934)

## Data

Gene col 2293: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2293); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2293, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2293]; `tensor/DDL_lfc|DDL_z.npy` [2293]; `embed/gene_vectors.npy` [2293]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2293 or target_col == 2293). Every well: [[PLLP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLLP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
