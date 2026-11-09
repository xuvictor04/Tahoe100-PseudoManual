---
symbol: "ZNF91"
type: "gene"
col: 9439
ensembl_id: "ENSG00000167232"
name: "zinc finger protein 91"
location: "19p12"
module: 23
arm: "+"
pooled_cpm: 64.29
n_lines_expressing: 44
n_dd_up: 8
n_dd_down: 5
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/023", "written"]
generated_by: "tahoemap"
---

# ZNF91

*zinc finger protein 91* — 19p12

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> ZNF91 is a primate-specific KRAB zinc-finger protein whose one well-established function is heterochromatic silencing of SVA retrotransposons.

## What it is

ZNF91 sits in the large KRAB zinc-finger cluster on chromosome 19, with the family's standard architecture: a KRAB domain that recruits TRIM28/SETDB1 to deposit H3K9me3, and a tandem zinc-finger array supplying specificity. Its array changed structurally in the hominid lineage roughly eight to twelve million years ago, including duplication of consecutive fingers, and the resulting protein recognises the VNTR of SVA elements — a retrotransposon family that expanded over the same period. Deleting ZNF91 in human embryonic stem cells reactivates SVAs, mainly young ones, together with a communal rise in other KZFP clusters. Outside transposon silencing and early development essentially nothing is established, and ZNF91 has no characterised protein-coding target promoters.

## What is uncertain

The inferred regulon is unlikely to be ZNF91's real target set: KZFPs act on repeat families through heterochromatin, not on individual protein-coding promoters, and a co-expression-derived regulon has no established relationship to that mechanism. ZNF91 also lies in a dense KZFP cluster whose members are co-expressed as a block — and whose coordinate upregulation is a documented consequence of SVA derepression — so both its measured level and its inferred activity partly report cluster-level transcription. The silencing work comes from embryonic stem cells; whether ZNF91 does anything comparable in differentiated cancer lines at 24 h is unknown.

## References

- Jacobs et al., 2014, Nature — identified ZNF91 and ZNF93 as KRAB zinc-finger repressors of SVA and L1 retrotransposons, and dated ZNF91's zinc-finger changes to the hominid lineage.
- Haring et al., 2021, Genome Research — CRISPR deletion of ZNF91 in human embryonic stem cells reactivated SVAs, chiefly young elements, and upregulated KRAB zinc-finger gene clusters.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.52× (z +10.1, q 3e-21, up in 33 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.666× (z -6.4, q 9e-08, down in 27 of 41 measured lines) ⚠ toxic; cell-cycle shift, explains ~33% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SNU-1 0.232×, H4 0.223×, RKO 0.444×, PANC-1 0.472×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 0.134×, SNU-1 0.146×, AN3 CA 0.220×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change); [[Digitoxin (drug)]] 5 µM in 3 lines (PANC-1 0.383×, NCI-H1792 0.343×, KATO III 0.397×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change); [[Mozavaptan (drug)]] 0.5 µM in 1 line (SW 1088 0.0761×); [[Bestatin (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1088 0.0844×); [[Niclosamide (olamine) (drug)]] 0.05 µM in 1 line (SW 1088 0.0767×).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARMCX5-GPRASP2]] (+0.70, fdr 1e-05), [[C11orf58]] (+0.70, fdr 4e-05), [[AEBP2]] (+0.69, fdr 3e-05); moves opposite to [[WDFY2]] (-0.58, fdr 7e-05), [[ARHGEF26]] (-0.58, fdr 1e-04), [[INPP5F]] (-0.57, fdr 5e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF737]] → it (grade B ⚠); 5 go from it, the strongest it → [[ZNF737]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9439.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +10.1 | 3e-21 | 33/42 (HOP62, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.45×** | +8.9 | 1e-16 | 37/42 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +6.0 | 3e-07 | 0/43 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +4.6 | 5e-04 | 25/42 (MIA PaCa-2, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.30×** | +4.5 | 1e-03 | 28/42 (LS 180, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.26×** | +4.0 | 0.006 | 26/42 (PANC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.29×** | +3.7 | 0.020 | 21/43 (LS 180, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +3.6 | 0.022 | 15/42 (LS 180, BT-474, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.029 | 21/41 (HEC-1-A, A498, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.046 | 14/43 (LS 180, SNU-423, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.22× | +3.1 | 0.11 | 16/42 (A498, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.11 | 14/42 (SNU-1, KATO III, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.21× | +3.0 | 0.11 | 16/42 (LS 180, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9439.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SNU-1 0.232×, H4 0.223×, RKO 0.444×, PANC-1 0.472×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 0.134×, SNU-1 0.146×, AN3 CA 0.220×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change); [[Digitoxin (drug)]] 5 µM in 3 lines (PANC-1 0.383×, NCI-H1792 0.343×, KATO III 0.397×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change); [[Mozavaptan (drug)]] 0.5 µM in 1 line (SW 1088 0.0761×); [[Bestatin (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1088 0.0844×); [[Niclosamide (olamine) (drug)]] 0.05 µM in 1 line (SW 1088 0.0767×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.666×** | -6.4 | 9e-08 | 27/41 (C-33 A, SK-MEL-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.697×** | -6.2 | 2e-07 | 31/42 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.681×** | -6.1 | 2e-07 | 21/38 (A-427, SNU-423, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.760×** | -4.7 | 3e-04 | 23/42 (SNU-1, H4, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | **0.780×** | -3.9 | 0.010 | 17/36 (SHP-77, SNU-1, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.828× | -3.2 | 0.11 | 16/42 (PANC-1, hTERT-HPNE, …) | rises with dose | composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | 0.712× | -3.0 | 0.19 | 16/42 (HCT15, BT-474, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9439. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 1088 (line)]] | alt | 96.3 | 0 | 4 (1 ⚠) | — | [[Mozavaptan (drug)]] 0.5 µM 0.0761× (z -9.4) |
| [[A-427 (line)]] | wt | 62.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.13× (z +10.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[PANC-1 (line)]] | alt | 64.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.74× (z +9.4) ⚠ cell-cycle shift, explains ~40% of this change | [[Digitoxin (drug)]] 5 µM 0.383× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[HepG2_C3A (line)]] | wt | 65.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[SK-MEL-2 (line)]] | alt | 90.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 134 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change |
| [[SNU-423 (line)]] | alt | 128 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.401× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[A498 (line)]] | wt | 20.8 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.44× (z +9.6) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[AN3 CA (line)]] | alt | 144 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change |
| [[C-33 A (line)]] | alt | 77.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.189× (z -13.7) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[H4 (line)]] | wt | 55.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 139 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +11.2) | — |
| [[HOP62 (line)]] | alt | 63.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +14.3) | — |
| [[J82 (line)]] | alt | 189 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.7) | — |
| [[KATO III (line)]] | alt | 69.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.397× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[LS 180 (line)]] | wt | 191 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.438× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[NCI-H1792 (line)]] | alt | 75.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.343× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[Panc 03.27 (line)]] | alt | 53.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +8.8) | — |
| [[RKO (line)]] | wt | 135 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 70.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change |
| [[SW480 (line)]] | alt | 68.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.6) | — |
| [[A-172 (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.76 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.52 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 101 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.75 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.97 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.42 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.01 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 97.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9439), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMCX5-GPRASP2]] | +0.70 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[C11orf58]] | +0.70 | +0.72 / +0.40 | both halves | 4e-05 |  |
| [[AEBP2]] | +0.69 | +0.68 / +0.43 | both halves | 3e-05 | same gene group |
| [[ZNF189]] | +0.68 | +0.68 / +0.48 | both halves | 2e-05 | same gene group |
| [[RAB30-DT]] | +0.68 | +0.76 / +0.37 | both halves | 8e-05 |  |
| [[ZNF253]] | +0.68 | +0.70 / +0.40 | both halves | 4e-05 | same gene group |
| [[ZNF606]] | +0.66 | +0.70 / +0.50 | both halves | 1e-05 | same gene group |
| [[ZNF407-AS1]] | +0.66 | +0.69 / +0.41 | both halves | 4e-05 |  |
| [[ZC3HC1]] | +0.66 | +0.70 / +0.45 | both halves | 3e-05 |  |
| [[METTL6]] | +0.65 | +0.70 / +0.35 | both halves | 1e-04 |  |
| [[ZNF701]] | +0.65 | +0.59 / +0.58 | both halves | 8e-06 | same gene group |
| [[RFX3-DT]] | +0.64 | +0.68 / +0.26 | both halves | 4e-04 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDFY2]] | -0.58 | -0.65 / -0.37 | both halves | 7e-05 |  |
| [[ARHGEF26]] | -0.58 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[INPP5F]] | -0.57 | -0.57 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF737]] | B | ZNF737 activity raises ZNF91's level | lines that do not express ZNF737 (18) vs lines expressing it (32) | 2.99× lower at baseline in the lines without ZNF737 | 0.004 | ⚠ within organs, on part of the lines; also absent: ZNF85, ZNF66, ZNF90 |
| [[ARMCX4]] | B | ARMCX4 activity raises ZNF91's level | lines that do not express ARMCX4 (18) vs lines expressing it (32) | 1.73× lower at baseline in the lines without ARMCX4 | 0.067 | ⚠ within organs, on part of the lines; also absent: TLR2, LYPD5, GALC |
| [[ZNF529-AS1]] | B | ZNF529-AS1 activity raises ZNF91's level | lines that do not express ZNF529-AS1 (8) vs lines expressing it (42) | 2.11× lower at baseline in the lines without ZNF529-AS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF529, HOMER2 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF737]] | B | ZNF91 activity raises ZNF737's level | lines that do not express ZNF91 (6) vs lines expressing it (44) | 3.71× lower at baseline in the lines without ZNF91 | 0.047 | ⚠ within organs, on part of the lines; also absent: ZNF493 |
| [[ZNF197]] | B | ZNF91 activity raises ZNF197's level | lines that do not express ZNF91 (6) vs lines expressing it (44) | 1.36× lower at baseline in the lines without ZNF91 | 0.074 | ⚠ within organs, on part of the lines; also absent: ZNF493 |
| [[ZKSCAN7-AS1]] | B | ZNF91 activity raises ZKSCAN7-AS1's level | lines that do not express ZNF91 (6) vs lines expressing it (44) | 1.51× lower at baseline in the lines without ZNF91 | 0.077 | ⚠ within organs, on part of the lines; also absent: ZNF493 |
| [[ARMCX4]] | B | ZNF91 activity raises ARMCX4's level | lines that do not express ZNF91 (6) vs lines expressing it (44) | 2.73× lower at baseline in the lines without ZNF91 | 0.081 | ⚠ within organs, on part of the lines; also absent: ZNF493 |
| [[ZNF117]] | B | ZNF91 activity raises ZNF117's level | lines that do not express ZNF91 (6) vs lines expressing it (44) | 1.62× lower at baseline in the lines without ZNF91 | 0.086 | ⚠ within organs, on part of the lines; also absent: ZNF493 |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.681). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-28.9, 15.4); signed map (17.8, -21.1). **Vector** length 80.2, 18.3% of its response variance represented; |z| ≥ 3 in 737 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +8.7 | +8.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.2 | +10.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +5.2 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +2.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.3 | +1.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +2.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -2.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.1 | -0.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -1.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -2.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | +1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.5 | -0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | +1.1 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 91 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p12 — chr19:23,304,991-23,395,471 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HPF7, HTF10 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q05481](https://www.uniprot.org/uniprotkb/Q05481) (Zinc finger protein 91):

> Transcription factor specifically required to repress SINE-VNTR-Alu (SVA) retrotransposons: recognizes and binds SVA sequences and represses their expression by recruiting a repressive complex containing TRIM28/KAP1. May also bind the promoter of the FCGR2B gene, leading to repress its expression; however, additional evidence is required to confirm this result in vivo.

**Summary**, from NCBI Gene [7644](https://www.ncbi.nlm.nih.gov/gene/7644):

> The ZNF91 gene encodes a zinc finger protein of the KRAB (Kruppel-associated box) subfamily (Bellefroid et al., 1991, 1993 [PubMed 2023909] [PubMed 8467795]).[supplied by OMIM, May 2010]

**Accessions** — [HGNC:13166](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13166) · Entrez [7644](https://www.ncbi.nlm.nih.gov/gene/7644) · UniProt [Q05481](https://www.uniprot.org/uniprotkb/Q05481) · Ensembl [ENSG00000167232](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167232)

## Data

Gene col 9439: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9439); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9439, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9439]; `tensor/DDL_lfc|DDL_z.npy` [9439]; `embed/gene_vectors.npy` [9439]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9439 or target_col == 9439). Every well: [[ZNF91 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/ZNF91.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
