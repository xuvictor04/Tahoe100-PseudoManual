---
symbol: "MRPL45"
type: "gene"
col: 15924
ensembl_id: "ENSG00000278845"
name: "mitochondrial ribosomal protein L45"
location: "17q12"
module: 64
arm: "+"
pooled_cpm: 28.4
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# MRPL45

*mitochondrial ribosomal protein L45* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.79× (z +8.8, q 1e-15, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.664× (z -6.5, q 4e-08, down in 29 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.699× (z -5.7, q 4e-06, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD4]] (+0.74, fdr 7e-06), [[PSMD7]] (+0.70, fdr 1e-05), [[UBXN4]] (+0.69, fdr 1e-05); moves opposite to [[C1QL1]] (-0.60, fdr 1e-04), [[PDXP]] (-0.58, fdr 5e-05), [[CALM3]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15924.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.79×** | +8.8 | 1e-15 | 40/48 (NCI-H1573, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.72×** | +8.7 | 1e-15 | 35/44 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.65×** | +8.0 | 3e-13 | 37/47 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.64×** | +7.9 | 5e-13 | 39/47 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +6.8 | 1e-09 | 22/36 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +6.1 | 1e-07 | 30/47 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +5.8 | 5e-07 | 29/47 (KATO III, HT-29, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +5.6 | 2e-06 | 26/47 (BT-474, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +5.4 | 5e-06 | 22/41 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.26×** | +5.1 | 2e-05 | 22/47 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.9 | 6e-05 | 19/48 (CFPAC-1, HS-578T, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.33×** | +4.6 | 2e-04 | 20/45 (HT-29, AsPC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.0 | 0.003 | 24/48 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.0 | 0.003 | 18/48 (NCI-H1573, KATO III, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.61×** | +4.0 | 0.003 | 15/41 (SK-MEL-2, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.039 | 10/47 (HS-578T, A498, …) | all doses, flat | low cells (technical?) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.060 | 12/46 (NCI-H1573, BT-474, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.074 | 15/48 (CFPAC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15924.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.664×** | -6.5 | 4e-08 | 29/46 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.699×** | -5.7 | 4e-06 | 28/47 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.757×** | -4.4 | 0.002 | 19/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.765×** | -4.2 | 0.003 | 17/48 (SW480, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Bergenin (drug)]] 5 µM |  | 0.844× | -3.8 | 0.016 | 16/48 (SNU-1, CFPAC-1, …) | rises with dose | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.796×** | -3.6 | 0.028 | 18/47 (LS 180, J82, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.800×** | -3.5 | 0.032 | 17/47 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **0.810×** | -3.3 | 0.058 | 16/47 (NCI-H460, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15924. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 35.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +10.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.438× (z -9.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 160 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.474× (z -8.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.475× (z -8.6) |
| [[A498 (line)]] | wt | 21.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 32.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +9.3) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 27.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.215× (z -8.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 64.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 18.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.131× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 22.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -8.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 20.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.69× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 18.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +9.6) ⚠ cell-cycle shift, explains ~24% of this change | — |
| [[NCI-H2030 (line)]] | alt | 41.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +8.7) ⚠ cell-cycle shift, explains ~24% of this change | — |
| [[SW1417 (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0679× (z -19.5) ⚠ toxic; cell-cycle shift, explains ~71% of this change |
| [[A-172 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15924), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD4]] | +0.74 | +0.83 / +0.63 | both halves | 7e-06 |  |
| [[PSMD7]] | +0.70 | +0.77 / +0.51 | both halves | 1e-05 |  |
| [[UBXN4]] | +0.69 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[TYW3]] | +0.69 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[ZNF189]] | +0.69 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[MRPL45P2]] | +0.68 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[PSMD6]] | +0.68 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[RHBDD3]] | +0.68 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[GATB]] | +0.67 | +0.77 / +0.53 | both halves | 1e-05 |  |
| [[DNAJC7]] | +0.67 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[PSMC5]] | +0.67 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[RNF6]] | +0.67 | +0.78 / +0.43 | both halves | 4e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1QL1]] | -0.60 | -0.60 / -0.35 | both halves | 1e-04 |  |
| [[PDXP]] | -0.58 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[CALM3]] | -0.57 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[NPTN]] | -0.56 | -0.64 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises MRPL45's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.764). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-19.4, 10.0); signed map (7.7, -30.8). **Vector** length 85.2, 18.1% of its response variance represented; |z| ≥ 3 in 800 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *proteasome* (control, mean cos +0.55 to 9); *Vif-mediated degradation of APOBEC3G* (reactome, mean cos +0.52 to 9); *Hedgehog 'on' state* (reactome, mean cos +0.51 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +7.6 | +8.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.9 | +8.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.6 | +7.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.6 | +6.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +5.4 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +4.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | +2.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.2 | -6.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | -3.7 | -3.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | -5.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.0 | -4.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -1.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.1 | +0.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L45 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:38,297,023-38,323,217 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC11321, Mba1, mL45 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRJ2](https://www.uniprot.org/uniprotkb/Q9BRJ2) (Large ribosomal subunit protein mL45):

> Component of the mitochondrial large ribosomal subunit (mt-LSU). Within the mitochondrial ribosomes, required to direct the nascent polypeptide toward the tunnel exit and position the exit at a distance from the membrane surface.

**Summary**, from NCBI Gene [84311](https://www.ncbi.nlm.nih.gov/gene/84311):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:16651](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16651) · Entrez [84311](https://www.ncbi.nlm.nih.gov/gene/84311) · UniProt [Q9BRJ2](https://www.uniprot.org/uniprotkb/Q9BRJ2) · Ensembl [ENSG00000278845](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000278845)

## Data

Gene col 15924: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15924); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15924, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15924]; `tensor/DDL_lfc|DDL_z.npy` [15924]; `embed/gene_vectors.npy` [15924]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15924 or target_col == 15924). Every well: [[MRPL45 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL45.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
