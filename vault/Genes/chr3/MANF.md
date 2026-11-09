---
symbol: "MANF"
type: "gene"
col: 6954
ensembl_id: "ENSG00000145050"
name: "mesencephalic astrocyte derived neurotrophic factor"
location: "3p21.2"
module: 42
arm: "+"
pooled_cpm: 48.86
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 10
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# MANF

*mesencephalic astrocyte derived neurotrophic factor* — 3p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.31× (z +9.4, q 3e-18, up in 43 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.81× (z +6.1, q 2e-07, up in 40 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 4.71×, NCI-H2030 3.33×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Auranofin (drug)]] 5 µM in 1 line (LOX-IMVI 4.51×).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.619× (z -6.3, q 1e-07, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMED9]] (+0.80, fdr 7e-06), [[SEC24D]] (+0.79, fdr 7e-06), [[PDIA4]] (+0.78, fdr 7e-06).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6954.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 4.71×, NCI-H2030 3.33×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Auranofin (drug)]] 5 µM in 1 line (LOX-IMVI 4.51×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.31×** | +9.4 | 3e-18 | 43/49 (HOP62, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.99×** | +7.1 | 4e-10 | 37/47 (A-427, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.81×** | +6.1 | 2e-07 | 40/48 (LOX-IMVI, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.64×** | +5.1 | 6e-05 | 33/48 (LOX-IMVI, A549, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.65×** | +5.0 | 8e-05 | 28/39 (NCI-H2030, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +3.7 | 0.018 | 25/47 (KATO III, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.40×** | +3.5 | 0.041 | 24/48 (LOX-IMVI, A549, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6954.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.619×** | -6.3 | 1e-07 | 30/47 (H4, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.608×** | -5.2 | 7e-05 | 32/48 (KATO III, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.631×** | -4.8 | 4e-04 | 29/48 (KATO III, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.648×** | -4.5 | 9e-04 | 30/48 (KATO III, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.724×** | -4.3 | 0.002 | 30/48 (HOP62, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~14% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.682×** | -4.0 | 0.007 | 27/48 (NCI-H2347, A-172, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.685×** | -3.9 | 0.007 | 24/48 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **0.713×** | -3.5 | 0.032 | 26/48 (RKO, A-172, …) | all doses, flat | position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | **0.771×** | -3.4 | 0.048 | 21/48 (HS-578T, C32, …) | rises with dose | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.731×** | -3.3 | 0.064 | 22/48 (HT-29, LS 180, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.744× | -3.1 | 0.11 | 18/48 (KATO III, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6954. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 149 | 0 | 8 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.169× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.267× (z -11.4) |
| [[A-172 (line)]] | wt | 80.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -11.6) |
| [[A-427 (line)]] | wt | 37.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -11.3) |
| [[H4 (line)]] | wt | 59.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -13.5) |
| [[HS-578T (line)]] | alt | 93.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 55.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H2030 (line)]] | alt | 46.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -10.1) |
| [[A498 (line)]] | wt | 46.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 23.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.51× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 34.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 62.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 69.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -10.7) |
| [[SHP-77 (line)]] | alt | 35.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -8.9) |
| [[A549 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 56.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 62.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 75.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 89.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 37.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6954), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED9]] | +0.80 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.79 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[PDIA4]] | +0.78 | +0.75 / +0.80 | both halves | 7e-06 | STRING 821 |
| [[GMPPA]] | +0.78 | +0.81 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[KDELR2]] | +0.78 | +0.75 / +0.72 | both halves | 7e-06 | STRING 546 |
| [[SEC61A1]] | +0.76 | +0.80 / +0.66 | both halves | 7e-06 |  |
| [[P4HB]] | +0.76 | +0.70 / +0.72 | both halves | 7e-06 | STRING 406 |
| [[HSP90B1]] | +0.75 | +0.72 / +0.77 | both halves | 7e-06 | STRING 831 |
| [[DNAJC3]] | +0.75 | +0.75 / +0.75 | both halves | 7e-06 | STRING 613 |
| [[HSPA5]] | +0.74 | +0.71 / +0.74 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation; STRING 996 |
| [[GORASP2]] | +0.74 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[COPB1]] | +0.74 | +0.75 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers MANF's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.786). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.1, -31.9); signed map (-53.5, 8.8). **Vector** length 125, 37.3% of its response variance represented; |z| ≥ 3 in 875 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.51 to 23); *Maturation of DENV proteins* (reactome, mean cos +0.64 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.63 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.1 | +6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +5.0 | +5.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +2.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.1 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[Lipoic acid (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -4.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.9 | -4.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.9 | -3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.6 | -4.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -5.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -1.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.2 | -2.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.2 | -3.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | mesencephalic astrocyte derived neurotrophic factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.2 — chr3:51,385,291-51,389,397 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARP; previously ARMET |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [P55145](https://www.uniprot.org/uniprotkb/P55145) (Mesencephalic astrocyte-derived neurotrophic factor):

> Selectively promotes the survival of dopaminergic neurons of the ventral mid-brain. Modulates GABAergic transmission to the dopaminergic neurons of the substantia nigra (By similarity). Enhances spontaneous, as well as evoked, GABAergic inhibitory postsynaptic currents in dopaminergic neurons (By similarity). Inhibits cell proliferation and endoplasmic reticulum (ER) stress-induced cell death. Retained in the ER/sarcoplasmic reticulum (SR) through association with the endoplasmic reticulum …

**Summary**, from NCBI Gene [7873](https://www.ncbi.nlm.nih.gov/gene/7873):

> The protein encoded by this gene is localized in the endoplasmic reticulum (ER) and golgi, and is also secreted. Reducing expression of this gene increases susceptibility to ER stress-induced death and results in cell proliferation. Activity of this protein is important in promoting the survival of dopaminergic neurons. The presence of polymorphisms in the N-terminal arginine-rich region, including a specific mutation that changes an ATG start codon to AGG, have been reported in a variety of …

**Accessions** — [HGNC:15461](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15461) · Entrez [7873](https://www.ncbi.nlm.nih.gov/gene/7873) · UniProt [P55145](https://www.uniprot.org/uniprotkb/P55145) · Ensembl [ENSG00000145050](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145050)

## Data

Gene col 6954: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6954); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6954, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6954]; `tensor/DDL_lfc|DDL_z.npy` [6954]; `embed/gene_vectors.npy` [6954]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6954 or target_col == 6954). Every well: [[MANF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MANF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
