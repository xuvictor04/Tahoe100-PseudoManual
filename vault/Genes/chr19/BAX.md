---
symbol: "BAX"
type: "gene"
col: 1483
ensembl_id: "ENSG00000087088"
name: "BCL2 associated X, apoptosis regulator"
location: "19q13.33"
module: 62
arm: "+"
pooled_cpm: 11.98
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 9
direction_downstream: 1
tags: ["gene", "module/062", "written"]
generated_by: "tahoemap"
---

# BAX

*BCL2 associated X, apoptosis regulator* — 19q13.33

> [!summary] In one line
> BAX is the pore-forming BCL-2-family effector that permeabilises the outer mitochondrial membrane, and it was the first component of the apoptotic machinery identified as a direct p53 transcriptional target.

## What it is

BAX is a multidomain pro-apoptotic member of the BCL-2 family. In healthy cells most of it is a soluble cytosolic monomer, cycling on and off mitochondria and being retrotranslocated back to the cytosol by anti-apoptotic relatives. On activation it undergoes a large conformational change, inserts into the outer mitochondrial membrane and oligomerises, with BAK, into macropores. That permeabilisation releases cytochrome c and SMAC, which assemble the APAF1 apoptosome and activate caspase-9 and then caspase-3. It is the commitment step of the intrinsic pathway: cells lacking both BAX and BAK are broadly resistant to mitochondrial apoptosis regardless of upstream signalling.

BAX is controlled at two levels. Transcriptionally, p53 binds its promoter and raises its expression, the finding that first put a p53 target inside the death machinery itself. Post-translationally — and this is where the decision is actually made — its activity depends on the balance between BH3-only activators such as BID, BIM and PUMA and the anti-apoptotic proteins BCL-2, BCL-xL and MCL-1 that sequester both activators and BAX. That stoichiometry is what BH3-mimetic drugs such as venetoclax exploit; they kill through BAX and BAK rather than around them. Frameshift mutations in the BAX coding repeat are recurrent in microsatellite-unstable colorectal cancer.

## What is uncertain

How much of a p53 transcriptional target BAX really is remains contested. The promoter work was done in a small number of systems, and across cell types BAX induction after p53 activation is usually modest and inconsistent, with PUMA and NOXA responding far more strongly; in several lineages BAX mRNA barely moves while apoptosis proceeds. So for this vault the direct-versus-indirect question is less interesting than the magnitude question: BAX is a genuine target whose transcriptional arm is probably not where its p53 dependence mostly lives. Mechanistically, whether PUMA and BID activate BAX directly or only by displacing it from anti-apoptotic partners is still argued, with evidence for both. The transcription-independent mechanism in which cytoplasmic p53 activates BAX directly is accepted by some groups and disputed by others. And Bax-null mice have a mild phenotype, which says BAK covers for it in most tissues.

## References

- Oltvai, Milliman and Korsmeyer, 1993, Cell — identified BAX as a BCL-2-interacting protein that promotes apoptosis.
- Miyashita and Reed, 1995, Cell — showed p53 is a direct transcriptional activator of the human BAX promoter.
- Wei et al., 2001, Science — showed BAX and BAK are jointly required for mitochondrial apoptosis.
- Chipuk et al., 2004, Science — reported direct activation of BAX by cytoplasmic p53, independent of transcription.
- Knudson et al., 1995, Science — characterised Bax-deficient mice, showing a limited phenotype consistent with redundancy.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.56× (z +13.7, q 7e-40, up in 31 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.63× (z +10.1, q 1e-21, up in 28 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Pentagastrin (drug)]] 5 µM: 0.828× (z -3.9, q 0.054, down in 7 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (SHP-77 0.0419×); [[Capmatinib (drug)]] 0.05 µM in 1 line (SHP-77 0.0683×); [[Digitoxin (drug)]] 5 µM in 1 line (KATO III 0.139×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idoxuridine (drug)]] 0.5 µM in 1 line (COLO 205 0.0659×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTCHD4]] (+0.74, fdr 7e-06), [[MDM2]] (+0.73, fdr 1e-05), [[ACTA2]] (+0.73, fdr 7e-06).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TP53]] → it (grade A ⚠); 1 goes from it, the strongest it → [[DDB2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1483.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.56×** | +13.7 | 7e-40 | 31/37 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.48×** | +12.2 | 6e-32 | 27/28 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +10.7 | 1e-24 | 19/23 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +10.1 | 1e-21 | 28/45 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +8.9 | 4e-17 | 28/41 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +6.3 | 2e-08 | 25/42 (Panc 03.27, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.9 | 2e-07 | 22/45 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.50×** | +5.9 | 3e-07 | 23/45 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +5.4 | 3e-06 | 18/48 (LoVo, LOX-IMVI, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.9 | 5e-05 | 17/44 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.25×** | +4.7 | 2e-04 | 17/47 (A549, NCI-H460, …) | rises with dose |  |
| [[Amsacrine (drug)]] 0.5 µM |  | **1.33×** | +4.1 | 0.002 | 17/48 (A549, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.8 | 0.007 | 17/46 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.016 | 14/46 (HT-29, SW1417, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.5 | 0.017 | 13/46 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.5 | 0.017 | 13/48 (LoVo, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Roxadustat (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.051 | 8/46 (NCI-H23, SW1417, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.082 | 14/46 (NCI-H460, A549, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1483.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (SHP-77 0.0419×); [[Capmatinib (drug)]] 0.05 µM in 1 line (SHP-77 0.0683×); [[Digitoxin (drug)]] 5 µM in 1 line (KATO III 0.139×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idoxuridine (drug)]] 0.5 µM in 1 line (COLO 205 0.0659×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pentagastrin (drug)]] 5 µM |  | **0.828×** | -3.9 | 0.054 | 7/48 (NCI-H23, SW1417, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -3.2 | 0.37 | 1/48 (COLO 205) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.865× | -3.0 | 0.38 | 14/48 (KATO III, RKO, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.675× | -3.0 | 0.38 | 5/44 (HepG2/C3A, NCI-H460, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1483. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +10.9) | — |
| [[LoVo (line)]] | wt | 11.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +10.7) | — |
| [[SHP-77 (line)]] | alt | 11.1 | 0 | 2 | — | [[Verteporfin (drug)]] 5 µM 0.0419× (z -14.3) |
| [[SW480 (line)]] | alt | 10.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.28× (z +11.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 4.16 | 0 | 1 | — | [[Captopril (drug)]] 0.05 µM 0.0753× (z -8.8) |
| [[COLO 205 (line)]] | alt | 6.95 | 0 | 1 | — | [[Idoxuridine (drug)]] 0.5 µM 0.0659× (z -9.4) |
| [[HS-578T (line)]] | alt | 9.38 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +11.7) | — |
| [[hTERT-HPNE (line)]] | wt | 19.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.139× (z -9.1) ⚠ transcription drop |
| [[KATO III (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.139× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 5.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 10.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.64× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.140× (z -11.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H2347 (line)]] | alt | 10.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +9.8) | — |
| [[A-172 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1483), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTCHD4]] | +0.74 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[MDM2]] | +0.73 | +0.55 / +0.73 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY; STRING 459 |
| [[ACTA2]] | +0.73 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[SPATA18]] | +0.72 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[EDA2R]] | +0.71 | +0.46 / +0.71 | both halves | 3e-05 |  |
| [[PINCR]] | +0.68 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[GRIN2C]] | +0.68 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[PHLDA3]] | +0.67 | +0.52 / +0.72 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[RRM2B]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[ZNF79]] | +0.66 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[TP53I3]] | +0.66 | +0.49 / +0.64 | both halves | 1e-05 | pathway: TP53 Regulates Transcription of Cell Death Genes |
| [[XPC]] | +0.65 | +0.73 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 1, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53]] | A | TP53 activity strengthens BAX's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 0.68× as strongly (z diff +1.00); strongest at Selinexor 5 µM: 1.10x vs 1.96x (z diff +4.1) | 6e-04 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers BAX's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[PINCR]] | B | PINCR activity strengthens BAX's drug response | lines that do not express PINCR (29) vs lines expressing it (19) | the lines without PINCR respond 0.73× as strongly (z diff +0.77); strongest at Selinexor 5 µM: 1.12x vs 1.80x (z diff +3.2) | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[GRIN2C]] | B | GRIN2C activity raises BAX's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 1.63× lower at baseline in the lines without GRIN2C | 0.011 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |
| [[ACTA2]] | B | ACTA2 activity raises BAX's level | lines that do not express ACTA2 (11) vs lines expressing it (39) | 1.50× lower at baseline in the lines without ACTA2 | 0.035 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent |
| [[EDA2R]] | B | EDA2R activity raises BAX's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.31× lower at baseline in the lines without EDA2R | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[FDXR]] | B | FDXR activity raises BAX's level | lines that do not express FDXR (8) vs lines expressing it (42) | 1.49× lower at baseline in the lines without FDXR | 0.086 | ⚠ within organs, on part of the lines; also absent: GRIN2C, MCM10; maybe low, not absent |
| [[TYMSOS]] | C | TYMSOS activity raises BAX's level | lines that do not express TYMSOS (3) vs lines expressing it (47) | 2.01× lower at baseline in the lines without TYMSOS | 0.051 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD4; also absent: FOXP4-AS1, ENSG00000261341, CCNP; maybe low, not absent |
| [[TP53]] | C | TP53 activity raises BAX's level | recorded loss-of-function mutation of TP53 in 33 lines vs 17 not recorded | 1.64× lower at baseline in the TP53-altered lines | 1.000 over the table, 0.091 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDB2]] | C | BAX's natural level strengthens DDB2's drug response | BAX's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.38; direction not clear | 0.043 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.776). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.8, 36.4); signed map (42.3, -23.7). **Vector** length 80.1, 15.0% of its response variance represented; |z| ≥ 3 in 887 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +5.4 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +13.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +10.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +3.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.2 | +4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.1 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +3.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.8 | +0.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -3.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +0.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.0 | -0.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.0 | -0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | +0.5 |
|  | [[Berbamine (dihydrochloride) (drug)]] 0.5 µM |  | -0.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | BCL2 associated X, apoptosis regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:48,954,815-48,961,798 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BCL2L4 |
| Gene groups (HGNC) | BCL2 family |
| Hallmark sets | APOPTOSIS, P53_PATHWAY, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 17 pathways, smallest: NTRK3 as a dependence receptor; Release of apoptotic factors from the mitochondria; Signaling by NTRK3 (TRKC) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07812](https://www.uniprot.org/uniprotkb/Q07812) (Apoptosis regulator BAX):

> Plays a role in the mitochondrial apoptotic process. Under normal conditions, BAX is largely cytosolic via constant retrotranslocation from mitochondria to the cytosol mediated by BCL2L1/Bcl-xL, which avoids accumulation of toxic BAX levels at the mitochondrial outer membrane (MOM). Under stress conditions, undergoes a conformation change that causes translocation to the mitochondrion membrane, leading to the release of cytochrome c that then triggers apoptosis. Promotes activation of CASP3, …

**Summary**, from NCBI Gene [581](https://www.ncbi.nlm.nih.gov/gene/581):

> The protein encoded by this gene belongs to the BCL2 protein family. BCL2 family members form hetero- or homodimers and act as anti- or pro-apoptotic regulators that are involved in a wide variety of cellular activities. This protein forms a heterodimer with BCL2, and functions as an apoptotic activator. The association and the ratio of BAX to BCL2 also determines survival or death of a cell following an apoptotic stimulus. This protein is reported to interact with, and increase the opening of, …

**Accessions** — [HGNC:959](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:959) · Entrez [581](https://www.ncbi.nlm.nih.gov/gene/581) · UniProt [Q07812](https://www.uniprot.org/uniprotkb/Q07812) · Ensembl [ENSG00000087088](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087088)

## Data

Gene col 1483: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1483); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1483, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1483]; `tensor/DDL_lfc|DDL_z.npy` [1483]; `embed/gene_vectors.npy` [1483]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1483 or target_col == 1483). Every well: [[BAX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/BAX.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
