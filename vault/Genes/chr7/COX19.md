---
symbol: "COX19"
type: "gene"
col: 14228
ensembl_id: "ENSG00000240230"
name: "cytochrome c oxidase assembly factor COX19"
location: "7p22.3"
module: 12
arm: "+"
pooled_cpm: 61.84
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# COX19

*cytochrome c oxidase assembly factor COX19* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.59× (z +9.6, q 6e-19, up in 26 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.41× (z +7.4, q 4e-11, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.597× (z -10.7, q 4e-24, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC1]] (+0.61, fdr 1e-05), [[DNAJC2]] (+0.61, fdr 1e-05), [[ZNF761]] (+0.57, fdr 1e-05); moves opposite to [[C4orf46]] (-0.53, fdr 2e-05), [[NAGA]] (-0.52, fdr 1e-05), [[EPB41L2]] (-0.51, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14228.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +9.6 | 6e-19 | 26/42 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +7.4 | 4e-11 | 35/48 (PANC-1, NCI-H2030, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +7.2 | 2e-10 | 34/47 (SW1417, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +4.8 | 2e-04 | 27/48 (NCI-H2347, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +4.7 | 3e-04 | 26/48 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.22×** | +4.0 | 0.005 | 18/45 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.059 | 13/48 (HT-29, J82, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.3 | 0.065 | 17/44 (MIA PaCa-2, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14228.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.597×** | -10.7 | 4e-24 | 32/48 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.735×** | -9.1 | 2e-17 | 29/49 (SW480, H4, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.692×** | -7.7 | 3e-12 | 33/50 (A-427, HOP62, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.819×** | -6.0 | 2e-07 | 24/47 (A498, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.763×** | -5.9 | 5e-07 | 28/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.769×** | -5.7 | 1e-06 | 24/48 (HT-29, HepG2/C3A, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.769×** | -5.5 | 3e-06 | 30/48 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.786×** | -5.2 | 1e-05 | 28/48 (SW480, RKO, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.779×** | -5.2 | 1e-05 | 27/47 (LoVo, C32, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.795×** | -5.0 | 4e-05 | 21/48 (SW480, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.802×** | -4.8 | 9e-05 | 23/48 (H4, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.873× | -4.1 | 0.002 | 15/48 (hTERT-HPNE, HT-29, …) | top dose only | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **0.833×** | -3.8 | 0.006 | 19/48 (SW480, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change | 0.851× | -3.5 | 0.019 | 18/48 (PANC-1, SW480, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14228. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 88.8 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -12.0) |
| [[HOP62 (line)]] | alt | 48.5 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -14.4) |
| [[AsPC-1 (line)]] | alt | 70.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.32× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -11.1) |
| [[H4 (line)]] | wt | 136 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 67.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.57× (z +10.7) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 54.0 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.331× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 71.7 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -12.7) |
| [[NCI-H460 (line)]] | wt | 48.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +17.7) | — |
| [[PANC-1 (line)]] | alt | 55.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.486× (z -9.8) |
| [[A-427 (line)]] | wt | 51.7 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -11.1) |
| [[A498 (line)]] | wt | 76.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -11.4) |
| [[HT-29 (line)]] | alt | 91.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.483× (z -8.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 80.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.505× (z -9.2) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 122 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.02× (z +9.2) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[Panc 03.27 (line)]] | alt | 65.8 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.176× (z -10.1) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 53.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SW 1088 (line)]] | alt | 73.8 | 0 | 1 | — | [[Drospirenone (drug)]] 0.05 µM 0.0772× (z -9.5) |
| [[SW 900 (line)]] | alt | 56.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SW1417 (line)]] | alt | 69.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.57× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 79.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 104 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 71.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 58.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 98.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14228), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC1]] | +0.61 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[DNAJC2]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[ZNF761]] | +0.57 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[TFAP2E]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[SRRM5]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[MPHOSPH10]] | +0.55 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[ZNF461]] | +0.55 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[PSMC1]] | +0.54 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[AAR2]] | +0.54 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[BRF2]] | +0.54 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[NDUFB9]] | +0.54 | +0.56 / +0.40 | both halves | 5e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[PCYT1A]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C4orf46]] | -0.53 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[NAGA]] | -0.52 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[EPB41L2]] | -0.51 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[PIGX]] | -0.51 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[RBBP7]] | -0.50 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[UBR5]] | -0.49 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[CDC25B]] | -0.49 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[STMN1]] | -0.48 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[SS18]] | -0.48 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[AGPAT1]] | -0.47 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[DPY19L1]] | -0.47 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[EZH2]] | -0.47 | -0.43 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers COX19's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises COX19's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.400). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-40.0, -1.7); signed map (-2.5, -17.0). **Vector** length 99.7, 23.0% of its response variance represented; |z| ≥ 3 in 809 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.4 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +7.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.2 | +4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.5 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.0 | +3.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.2 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +1.9 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -7.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -10.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -9.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.2 | -5.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change | -2.7 | -3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -5.5 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.3 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.9 | -1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.8 | -1.1 |
|  | [[Adenine (drug)]] 5 µM |  | -1.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase assembly factor COX19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:898,778-975,549 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC104475 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 5 pathways, smallest: Complex IV assembly; Mitochondrial protein import; Respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q49B96](https://www.uniprot.org/uniprotkb/Q49B96) (Cytochrome c oxidase assembly protein COX19):

> Assembly factor for cytochrome c oxidase (respiratory chain complex IV, CIV). Acts as a COX11 chaperone that supports COX11 copper coordination. Also stimulates SCO2-mediated metalation of COX2. Required for the transduction of an SCO1-dependent redox signal from the mitochondrion to ATP7A to regulate cellular copper homeostasis. In the absence of COX11, capable of stimulating copper delivery to the copper B site of COX1.

**Summary**, from NCBI Gene [90639](https://www.ncbi.nlm.nih.gov/gene/90639):

> COX19 encodes a cytochrome c oxidase (COX)-assembly protein. The S. cerevisiae Cox19 protein may play a role in metal transport to the mitochondrial intermembrane space and assembly of complex IV of the mitochondrial respiratory chain (Sacconi et al., 2005 [PubMed 16212937]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:28074](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28074) · Entrez [90639](https://www.ncbi.nlm.nih.gov/gene/90639) · UniProt [Q49B96](https://www.uniprot.org/uniprotkb/Q49B96) · Ensembl [ENSG00000240230](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240230)

## Data

Gene col 14228: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14228); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14228, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14228]; `tensor/DDL_lfc|DDL_z.npy` [14228]; `embed/gene_vectors.npy` [14228]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14228 or target_col == 14228). Every well: [[COX19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COX19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
