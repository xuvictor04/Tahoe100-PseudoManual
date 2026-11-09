---
symbol: "SNRPD2"
type: "gene"
col: 4655
ensembl_id: "ENSG00000125743"
name: "small nuclear ribonucleoprotein D2 polypeptide"
location: "19q13.2-q13.3"
module: 131
arm: "+"
pooled_cpm: 68.37
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# SNRPD2

*small nuclear ribonucleoprotein D2 polypeptide* — 19q13.2-q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.71× (z +7.7, q 6e-12, up in 41 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Arbutin (drug)]] 5 µM: 1.50× (z +3.2, q 0.087, up in 37 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H1573 4.77×, SW480 4.18×, Hs 766T 4.49×, NCI-H460 4.01×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.604× (z -5.7, q 6e-06, down in 38 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SNU-1 0.169×, C-33 A 0.313×, KATO III 0.431×); [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H596 0.121×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS21]] (+0.83, fdr 7e-06), [[COX6A1]] (+0.83, fdr 7e-06), [[UQCRH]] (+0.81, fdr 7e-06); moves opposite to [[TIA1]] (-0.72, fdr 1e-05), [[ARFGAP2]] (-0.70, fdr 1e-05), [[EIF4G2]] (-0.69, fdr 1e-05).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 9 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4655.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H1573 4.77×, SW480 4.18×, Hs 766T 4.49×, NCI-H460 4.01×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.71×** | +7.7 | 6e-12 | 41/43 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **3.36×** | +7.4 | 5e-11 | 45/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **2.04×** | +5.7 | 2e-06 | 44/47 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.98×** | +5.5 | 5e-06 | 47/48 (HOP62, NCI-H1573, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.09×** | +5.5 | 5e-06 | 37/45 (KATO III, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +5.0 | 6e-05 | 43/47 (CFPAC-1, RKO, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.70×** | +4.3 | 0.001 | 39/48 (NCI-H1573, COLO 205, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.60×** | +3.8 | 0.012 | 34/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **1.56×** | +3.6 | 0.022 | 35/48 (NCI-H1573, PANC-1, …) | top dose only | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **1.50×** | +3.2 | 0.087 | 37/48 (NCI-H2030, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4655.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SNU-1 0.169×, C-33 A 0.313×, KATO III 0.431×); [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H596 0.121×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.604×** | -5.7 | 6e-06 | 38/48 (SNU-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4655. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 87.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.40× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -8.7) |
| [[C-33 A (line)]] | alt | 74.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -9.9) |
| [[Hs 766T (line)]] | wt | 50.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.49× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H1573 (line)]] | alt | 50.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.77× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H1792 (line)]] | alt | 59.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.87× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H460 (line)]] | wt | 41.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.01× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H596 (line)]] | alt | 64.7 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.121× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 58.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.01× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SNU-1 (line)]] | wt | 55.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -13.4) |
| [[SW480 (line)]] | alt | 76.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.18× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[A-172 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 93.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 83.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 82.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 64.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 70.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 97.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 54.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4655), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 10 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS21]] | +0.83 | +0.78 / +0.81 | both halves | 7e-06 | pathway: SARS-CoV-2 Infection; STRING 558 |
| [[COX6A1]] | +0.83 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[UQCRH]] | +0.81 | +0.76 / +0.75 | both halves | 7e-06 | STRING 491 |
| [[RPS5]] | +0.81 | +0.74 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 617 |
| [[RPS25]] | +0.80 | +0.74 / +0.78 | both halves | 7e-06 | pathway: SARS-CoV-2 Infection; STRING 471 |
| [[ANAPC11]] | +0.79 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[RPLP2]] | +0.78 | +0.73 / +0.80 | both halves | 7e-06 | STRING 553 |
| [[RPS14]] | +0.78 | +0.76 / +0.77 | both halves | 7e-06 | pathway: SARS-CoV-2 Infection; STRING 468 |
| [[RPL27A]] | +0.78 | +0.77 / +0.78 | both halves | 7e-06 |  |
| [[RPL28]] | +0.77 | +0.72 / +0.78 | both halves | 7e-06 |  |
| [[RPL32]] | +0.77 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[ELOB]] | +0.77 | +0.68 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIA1]] | -0.72 | -0.70 / -0.54 | both halves | 1e-05 | STRING 520 |
| [[ARFGAP2]] | -0.70 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.69 | -0.49 / -0.60 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[PCNX4-DT]] | -0.69 | -0.62 / -0.32 | both halves | 2e-04 |  |
| [[TRIP6]] | -0.67 | -0.64 / -0.37 | both halves | 8e-05 |  |
| [[SEPTIN8]] | -0.66 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[C19orf54]] | -0.66 | -0.67 / -0.26 | both halves | 3e-04 | STRING 921 |
| [[ZNF747]] | -0.65 | -0.59 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers SNRPD2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.777). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-48.3, -25.7); signed map (-56.0, -3.5). **Vector** length 74.1, 29.2% of its response variance represented; |z| ≥ 3 in 545 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Termination* (reactome, mean cos +0.72 to 20); *Peptide chain elongation* (reactome, mean cos +0.73 to 19); *PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA* (reactome, mean cos +0.73 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +4.0 | +5.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +3.7 | +3.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +3.6 | +4.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +0.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +0.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | +1.3 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | -0.3 |
|  | [[NVP-BHG712 (drug)]] 0.05 µM |  | +1.1 | -1.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.5 | -5.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | -2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -4.7 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -4.6 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | -4.5 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -0.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.9 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | small nuclear ribonucleoprotein D2 polypeptide |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2-q13.3 — chr19:45,687,460-45,692,569 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Sm-D2; previously SNRPD1 |
| Gene groups (HGNC) | Sm spliceosomal proteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 20 pathways, smallest: SARS-CoV-2 modulates host translation machinery; mRNA Splicing - Minor Pathway; Metabolism of non-coding RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [P62316](https://www.uniprot.org/uniprotkb/P62316) (Small nuclear ribonucleoprotein Sm D2):

> Plays a role in pre-mRNA splicing as a core component of the spliceosomal U1, U2, U4 and U5 small nuclear ribonucleoproteins (snRNPs), the building blocks of the spliceosome. Component of both the pre-catalytic spliceosome B complex and activated spliceosome C complexes. As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs.

**Summary**, from NCBI Gene [6633](https://www.ncbi.nlm.nih.gov/gene/6633):

> The protein encoded by this gene belongs to the small nuclear ribonucleoprotein core protein family. It is required for pre-mRNA splicing and small nuclear ribonucleoprotein biogenesis. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, May 2009]

**Accessions** — [HGNC:11159](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11159) · Entrez [6633](https://www.ncbi.nlm.nih.gov/gene/6633) · UniProt [P62316](https://www.uniprot.org/uniprotkb/P62316) · Ensembl [ENSG00000125743](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125743)

## Data

Gene col 4655: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4655); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4655, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4655]; `tensor/DDL_lfc|DDL_z.npy` [4655]; `embed/gene_vectors.npy` [4655]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4655 or target_col == 4655). Every well: [[SNRPD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNRPD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
