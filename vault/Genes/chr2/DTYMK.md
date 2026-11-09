---
symbol: "DTYMK"
type: "gene"
col: 9640
ensembl_id: "ENSG00000168393"
name: "deoxythymidylate kinase"
location: "2q37.3"
module: 67
arm: "+"
pooled_cpm: 23.31
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# DTYMK

*deoxythymidylate kinase* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.23× (z +12.0, q 4e-30, up in 41 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Palmatine (chloride) (drug)]] 0.5 µM: 1.43× (z +3.7, q 0.018, up in 20 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.534× (z -8.7, q 2e-15, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OIP5]] (+0.82, fdr 7e-06), [[KIF22]] (+0.82, fdr 7e-06), [[MELK]] (+0.81, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9640.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **3.23×** | +12.0 | 4e-30 | 41/43 (A-172, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.57×** | +9.3 | 6e-18 | 31/33 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **2.00×** | +7.0 | 3e-10 | 36/44 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.97×** | +6.4 | 2e-08 | 29/39 (A-172, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +4.4 | 0.001 | 21/43 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.35×** | +4.1 | 0.004 | 29/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~69% of this change | **1.48×** | +3.8 | 0.010 | 23/47 (H4, A-172, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.43×** | +3.7 | 0.018 | 20/47 (H4, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.064 | 21/46 (COLO 205, NCI-H1573, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **2.00×** | +3.3 | 0.064 | 22/47 (SW480, NCI-H1792, …) | all doses, flat | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.2 | 0.072 | 18/47 (A549, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9640.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.534×** | -8.7 | 2e-15 | 38/47 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.605×** | -5.1 | 1e-04 | 32/48 (A498, LS 180, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.636×** | -4.6 | 8e-04 | 26/47 (MIA PaCa-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.738×** | -4.2 | 0.004 | 22/48 (A498, HCT15, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.326×** | -4.1 | 0.004 | 27/46 (NCI-H460, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.694×** | -3.7 | 0.020 | 22/48 (NCI-H661, HOP62, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.407×** | -3.3 | 0.078 | 16/48 (A-427, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.787×** | -3.3 | 0.080 | 22/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~76% of this change | 0.735× | -3.1 | 0.11 | 19/48 (HT-29, SNU-1, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.724× | -3.1 | 0.11 | 19/48 (KATO III, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.436× | -3.0 | 0.12 | 10/47 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9640. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 31.5 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Selinexor (drug)]] 5 µM 0.326× (z -11.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 35.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.89× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 20.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0850× (z -14.0) |
| [[NCI-H23 (line)]] | alt | 37.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -9.6) |
| [[PANC-1 (line)]] | alt | 36.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.27× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[SW480 (line)]] | alt | 26.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -9.6) |
| [[KATO III (line)]] | alt | 23.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[LS 180 (line)]] | wt | 23.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.31× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H1792 (line)]] | alt | 21.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.10× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[RPMI-7951 (line)]] | alt | 25.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.33× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[SNU-1 (line)]] | wt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.108× (z -8.5) |
| [[SNU-423 (line)]] | alt | 13.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.88× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SW1417 (line)]] | alt | 25.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[A-427 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9640), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OIP5]] | +0.82 | +0.76 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[KIF22]] | +0.82 | +0.75 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[MELK]] | +0.81 | +0.83 / +0.73 | both halves | 7e-06 |  |
| [[POC1A]] | +0.80 | +0.81 / +0.77 | both halves | 7e-06 |  |
| [[SPC25]] | +0.79 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[VRK1]] | +0.79 | +0.83 / +0.70 | both halves | 7e-06 |  |
| [[AURKB]] | +0.79 | +0.72 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[WDR62]] | +0.78 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[SPC24]] | +0.78 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[NSD2]] | +0.78 | +0.78 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[PBK]] | +0.77 | +0.75 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[KIF15]] | +0.77 | +0.72 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.833). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-34.7, -51.0); signed map (-43.4, -42.2). **Vector** length 75.4, 19.9% of its response variance represented; |z| ≥ 3 in 669 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.73 to 12); *Mitotic Prometaphase* (reactome, mean cos +0.71 to 8); *Deposition of new CENPA-containing nucleosomes at the centromere* (reactome, mean cos +0.69 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | +0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +1.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.3 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +2.1 | +12.0 |
|  | [[vincristine (drug)]] 5 µM |  | +1.3 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.3 | +3.3 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +1.3 | +2.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.2 | +0.2 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | -4.7 | -5.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.1 | -4.2 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~76% of this change | -3.2 | -3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -0.8 |
|  | [[palbociclib (drug)]] 5 µM |  | -1.5 | -0.1 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | deoxythymidylate kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:241,675,747-241,686,944 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDC8, TYMK, TMPK |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 2 pathways, smallest: Interconversion of nucleotide di- and triphosphates; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [P23919](https://www.uniprot.org/uniprotkb/P23919) (Thymidylate kinase):

> Catalyzes the phosphorylation of thymidine monophosphate (dTMP) to thymidine diphosphate (dTDP), the immediate precursor for the DNA building block dTTP, with ATP as the preferred phosphoryl donor in the presence of Mg(2+).

**Summary**, from NCBI Gene [1841](https://www.ncbi.nlm.nih.gov/gene/1841):

> Enables ATP binding activity and dTMP kinase activity. Involved in dTDP biosynthetic process and thymidine biosynthetic process. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:3061](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3061) · Entrez [1841](https://www.ncbi.nlm.nih.gov/gene/1841) · UniProt [P23919](https://www.uniprot.org/uniprotkb/P23919) · Ensembl [ENSG00000168393](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168393)

## Data

Gene col 9640: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9640); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9640, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9640]; `tensor/DDL_lfc|DDL_z.npy` [9640]; `embed/gene_vectors.npy` [9640]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9640 or target_col == 9640). Every well: [[DTYMK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DTYMK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
