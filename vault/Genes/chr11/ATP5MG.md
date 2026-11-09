---
symbol: "ATP5MG"
type: "gene"
col: 9447
ensembl_id: "ENSG00000167283"
name: "ATP synthase membrane subunit g"
location: "11q23.3"
module: 131
arm: "+"
pooled_cpm: 68.2
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# ATP5MG

*ATP synthase membrane subunit g* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.32× (z +9.7, q 3e-19, up in 47 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +4.8, q 2e-04, up in 38 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP5F1E]] (+0.75, fdr 7e-06), [[RPS29]] (+0.74, fdr 7e-06), [[NDUFA4]] (+0.73, fdr 7e-06); moves opposite to [[EIF4G1]] (-0.65, fdr 1e-05), [[PSMG1]] (-0.60, fdr 4e-05), [[PUF60]] (-0.59, fdr 6e-05).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9447.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **4.32×** | +9.7 | 3e-19 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **3.25×** | +8.6 | 3e-15 | 38/41 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.70×** | +6.9 | 1e-09 | 42/45 (KATO III, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.40×** | +6.6 | 5e-09 | 46/47 (COLO 205, PANC-1, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +4.8 | 2e-04 | 44/47 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +4.8 | 2e-04 | 38/48 (NCI-H2347, SNU-423, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.86×** | +4.7 | 2e-04 | 42/47 (BT-474, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.68×** | +3.9 | 0.006 | 39/48 (COLO 205, SW480, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.62×** | +3.6 | 0.018 | 41/48 (NCI-H23, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.56×** | +3.2 | 0.070 | 29/50 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +3.1 | 0.085 | 37/48 (RPMI-7951, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sulfatinib (drug)]] 5 µM |  | **1.54×** | +3.1 | 0.085 | 34/48 (SNU-423, NCI-H2030, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.52×** | +3.0 | 0.097 | 33/48 (A-172, HOP62, …) | top dose only | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **1.52×** | +3.0 | 0.097 | 38/48 (A549, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.49×** | +3.0 | 0.099 | 29/48 (A-172, NCI-H1573, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9447.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sapanisertib (drug)]] 5 µM |  | 0.437× | -3.2 | 0.70 | 36/49 (HEC-1-A, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9447. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 39.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.19× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[HOP62 (line)]] | alt | 37.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 35.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.01× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H1792 (line)]] | alt | 37.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.30× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H460 (line)]] | wt | 51.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.65× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[PANC-1 (line)]] | alt | 116 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.13× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SW480 (line)]] | alt | 76.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-172 (line)]] | wt | 38.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A498 (line)]] | wt | 55.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[C-33 A (line)]] | alt | 63.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.62× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[C32 (line)]] | wt | 78.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.86× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HT-29 (line)]] | alt | 100 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.47× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[KATO III (line)]] | alt | 132 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[LoVo (line)]] | wt | 71.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H23 (line)]] | alt | 55.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H2347 (line)]] | alt | 86.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +8.6) | — |
| [[RKO (line)]] | wt | 78.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SNU-423 (line)]] | alt | 51.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.73× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-427 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 58.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 72.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 65.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 75.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 98.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 61.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 69.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9447), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 17 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5F1E]] | +0.75 | +0.69 / +0.73 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[RPS29]] | +0.74 | +0.60 / +0.76 | both halves | 7e-06 | STRING 486 |
| [[NDUFA4]] | +0.73 | +0.65 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 886 |
| [[COPS9]] | +0.73 | +0.75 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[RPLP2]] | +0.73 | +0.57 / +0.77 | both halves | 9e-06 |  |
| [[RPL38]] | +0.73 | +0.56 / +0.75 | both halves | 1e-05 |  |
| [[COX7B]] | +0.72 | +0.64 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 786 |
| [[RPS11]] | +0.72 | +0.53 / +0.75 | both halves | 1e-05 |  |
| [[RPS21]] | +0.71 | +0.53 / +0.78 | both halves | 1e-05 |  |
| [[SNHG25]] | +0.71 | +0.52 / +0.73 | both halves | 1e-05 |  |
| [[COX4I1]] ⚠ | +0.71 | +0.62 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 765; ⚠ in the vector space only through flagged drug-doses |
| [[RPL36A]] | +0.71 | +0.55 / +0.76 | both halves | 1e-05 |  |
| [[MZT2B]] | +0.70 | +0.53 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G1]] | -0.65 | -0.49 / -0.70 | both halves | 1e-05 |  |
| [[PSMG1]] | -0.60 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[PUF60]] | -0.59 | -0.38 / -0.66 | both halves | 6e-05 |  |
| [[ZNF460]] | -0.59 | -0.38 / -0.67 | both halves | 7e-05 |  |
| [[PDAP1]] | -0.58 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[TMEM185B]] | -0.56 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[PRMT5]] | -0.56 | -0.48 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ATP5MG's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.748). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-47.3, -24.1); signed map (-61.8, -1.6). **Vector** length 61.4, 22.5% of its response variance represented; |z| ≥ 3 in 615 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Termination* (reactome, mean cos +0.66 to 20); *Peptide chain elongation* (reactome, mean cos +0.67 to 19); *PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA* (reactome, mean cos +0.67 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +2.7 | +6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +2.3 | +3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +2.0 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.7 | +2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | -0.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.4 | +1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +1.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +0.4 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.7 | +2.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | -3.5 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | +1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -3.5 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -3.4 | +6.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | +0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | +1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | ATP synthase membrane subunit g |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:118,401,346-118,433,278 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ATP5JG; previously ATP5L |
| Gene groups (HGNC) | Mitochondrial complex V: ATP synthase subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 6 pathways, smallest: Formation of ATP by chemiosmotic coupling; Cristae formation; Mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [O75964](https://www.uniprot.org/uniprotkb/O75964) (ATP synthase F(0) complex subunit g, mitochondrial):

> Subunit g, of the mitochondrial membrane ATP synthase complex (F(1)F(0) ATP synthase or Complex V) that produces ATP from ADP in the presence of a proton gradient across the membrane which is generated by electron transport complexes of the respiratory chain. ATP synthase complex consist of a soluble F(1) head domain - the catalytic core - and a membrane F(1) domain - the membrane proton channel. These two domains are linked by a central stalk rotating inside the F(1) region and a stationary …

**Summary**, from NCBI Gene [10632](https://www.ncbi.nlm.nih.gov/gene/10632):

> Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. It is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, which comprises the proton channel. The F1 complex consists of 5 different subunits (alpha, beta, gamma, delta, and epsilon) assembled in a ratio of 3 alpha, 3 beta, and a single representative of the other 3. …

**Accessions** — [HGNC:14247](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14247) · Entrez [10632](https://www.ncbi.nlm.nih.gov/gene/10632) · UniProt [O75964](https://www.uniprot.org/uniprotkb/O75964) · Ensembl [ENSG00000167283](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167283)

## Data

Gene col 9447: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9447); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9447, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9447]; `tensor/DDL_lfc|DDL_z.npy` [9447]; `embed/gene_vectors.npy` [9447]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9447 or target_col == 9447). Every well: [[ATP5MG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP5MG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
