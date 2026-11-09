---
symbol: "INO80B"
type: "gene"
col: 3648
ensembl_id: "ENSG00000115274"
name: "INO80 complex subunit B"
location: "2p13.1"
module: 69
arm: "+"
pooled_cpm: 11.93
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 5
n_dd_up_clean: 25
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# INO80B

*INO80 complex subunit B* — 2p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.10× (z +14.6, q 3e-45, up in 42 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Carbidopa (monohydrate) (drug)]] 0.05 µM: 0.595× (z -7.1, q 6e-10, down in 38 of 47 measured lines) ⚠ unreliable plate only; position not correctable. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.708× (z -4.7, q 4e-04, down in 19 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF2F1]] (+0.60, fdr 1e-05), [[NR1H2]] (+0.59, fdr 3e-05), [[ST13]] (+0.54, fdr 4e-05); moves opposite to [[PFN1]] (-0.48, fdr 2e-04), [[EEFSEC]] (-0.46, fdr 1e-04), [[SPTSSA]] (-0.44, fdr 5e-04).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3648.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +14.6 | 3e-45 | 42/45 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +8.6 | 2e-15 | 23/30 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +8.1 | 1e-13 | 27/36 (HEC-1-A, A498, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.83×** | +7.9 | 3e-13 | 31/45 (A-427, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.71×** | +7.5 | 1e-11 | 33/46 (A-427, PANC-1, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +7.0 | 3e-10 | 32/47 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +6.6 | 2e-09 | 15/21 (LOX-IMVI, SW1417, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.59×** | +6.5 | 7e-09 | 33/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +6.3 | 2e-08 | 27/48 (HOP62, PANC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +6.2 | 2e-08 | 25/45 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +6.2 | 2e-08 | 29/47 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +5.6 | 1e-06 | 21/44 (C-33 A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +5.4 | 3e-06 | 22/47 (A-427, PANC-1, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.91×** | +4.7 | 1e-04 | 17/47 (LoVo, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.40×** | +4.7 | 1e-04 | 21/44 (RPMI-7951, H4, …) | all doses, flat | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.6 | 2e-04 | 18/45 (C-33 A, A-427, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +4.2 | 8e-04 | 16/46 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.002 | 16/47 (NCI-H2030, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3648.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.595×** | -7.1 | 6e-10 | 38/47 (A498, A549, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.699×** | -4.9 | 3e-04 | 21/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.708×** | -4.7 | 4e-04 | 19/47 (COLO 205, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.753×** | -3.9 | 0.014 | 12/46 (A-172, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.763×** | -3.7 | 0.023 | 12/47 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.796× | -3.1 | 0.16 | 14/44 (HCT15, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 0.798× | -3.1 | 0.16 | 10/43 (HEC-1-A, HCT15, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3648. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 8.90 | 0 | 2 | — | [[Entecavir (monohydrate) (drug)]] 0.05 µM 0.0891× (z -9.6) |
| [[BT-474 (line)]] | alt | 7.17 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0784× (z -8.9) |
| [[C-33 A (line)]] | alt | 12.8 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.130× (z -8.5) |
| [[C32 (line)]] | wt | 7.83 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.0735× (z -10.3) |
| [[HCT15 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0744× (z -11.2) ⚠ transcription drop |
| [[NCI-H23 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.136× (z -10.5) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 8.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +8.6) | — |
| [[SW480 (line)]] | alt | 10.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +9.5) | — |
| [[A-172 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3648), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2F1]] | +0.60 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[NR1H2]] | +0.59 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[ST13]] | +0.54 | +0.70 / +0.41 | both halves | 4e-05 |  |
| [[OSER1]] | +0.54 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[YPEL5]] | +0.54 | +0.33 / +0.59 | both halves | 1e-04 |  |
| [[HBP1]] | +0.53 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[CALCOCO1]] | +0.53 | +0.39 / +0.60 | both halves | 5e-05 |  |
| [[EPM2AIP1]] | +0.53 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[TBC1D15]] | +0.52 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[PRPF18]] | +0.51 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[WBP1]] | +0.51 | +0.40 / +0.58 | both halves | 5e-05 | ⚠ same locus (0.5 kb, same strand: neighbours can correlate without regulation) |
| [[VSIG10L]] | +0.51 | +0.38 / +0.46 | both halves | 6e-05 |  |
| [[NUCB1]] | +0.51 | +0.40 / +0.55 | both halves | 5e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PFN1]] | -0.48 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[EEFSEC]] | -0.46 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[SPTSSA]] | -0.44 | -0.45 / -0.24 | both halves | 5e-04 |  |
| [[SKA1]] | -0.44 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[CYC1]] | -0.43 | -0.32 / -0.28 | both halves | 3e-04 |  |
| [[H2AZ1]] | -0.43 | -0.49 / -0.27 | both halves | 3e-04 |  |
| [[CEP85]] | -0.43 | -0.40 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers INO80B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.420). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.5, -52.0); signed map (-3.2, -5.9). **Vector** length 68.0, 11.0% of its response variance represented; |z| ≥ 3 in 880 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +14.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.5 | +7.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.0 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +8.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.0 | +7.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.3 | +4.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +2.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.1 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +6.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.3 | -3.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -1.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | INO80 complex subunit B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.1 — chr2:74,455,087-74,457,944 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HMGIYL4, PAPA-1, hIes2, PAP-1BP, IES2; previously HMGA1L4, ZNHIT4 |
| Gene groups (HGNC) | Zinc fingers HIT-type; INO80 complex subunits |
| Reactome | 6 pathways, smallest: DNA Damage Recognition in GG-NER; UCH proteinases; Global Genome Nucleotide Excision Repair (GG-NER) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C086](https://www.uniprot.org/uniprotkb/Q9C086) (INO80 complex subunit B):

> Induces growth and cell cycle arrests at the G1 phase of the cell cycle.; Proposed core component of the chromatin remodeling INO80 complex which is involved in transcriptional regulation, DNA replication and probably DNA repair.

**Summary**, from NCBI Gene [83444](https://www.ncbi.nlm.nih.gov/gene/83444):

> This gene encodes a subunit of an ATP-dependent chromatin remodeling complex, INO80, which plays a role in DNA and nucleosome-activated ATPase activity and ATP-dependent nucleosome sliding. Readthrough transcription of this gene into the neighboring downstream gene, which encodes WW domain-binding protein 1, generates a non-coding transcript. [provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:13324](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13324) · Entrez [83444](https://www.ncbi.nlm.nih.gov/gene/83444) · UniProt [Q9C086](https://www.uniprot.org/uniprotkb/Q9C086) · Ensembl [ENSG00000115274](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115274)

## Data

Gene col 3648: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3648); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3648, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3648]; `tensor/DDL_lfc|DDL_z.npy` [3648]; `embed/gene_vectors.npy` [3648]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3648 or target_col == 3648). Every well: [[INO80B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INO80B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
