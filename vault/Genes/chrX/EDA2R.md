---
symbol: "EDA2R"
type: "gene"
col: 5167
ensembl_id: "ENSG00000131080"
name: "ectodysplasin A2 receptor"
location: "Xq12"
module: 62
arm: "+"
pooled_cpm: 8.82
n_lines_expressing: 22
n_dd_up: 26
n_dd_down: 7
n_dd_up_clean: 17
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 10
direction_downstream: 27
tags: ["gene", "module/062", "written"]
generated_by: "tahoemap"
---

# EDA2R

*ectodysplasin A2 receptor* — Xq12

> [!summary] In one line
> EDA2R, also called XEDAR or TNFRSF27, is an X-linked TNF-receptor-family receptor for the EDA-A2 isoform of ectodysplasin A, one of the most steeply p53-inducible transcripts in the genome, and an emerging marker of muscle wasting and ageing.

## What it is

EDA2R is a membrane receptor of the TNF receptor superfamily, encoded on the X chromosome. It is the receptor for EDA-A2, one of two splice isoforms of ectodysplasin A; a two-amino-acid difference in the ligand determines whether it binds EDAR (EDA-A1) or EDA2R (EDA-A2), one of the cleanest examples of a splice-level switch between two receptors. Unlike most TNFRSF members with cytotoxic activity, EDA2R has no death domain. It couples instead to NF-κB and JNK signalling, and in overexpression systems has been reported to drive caspase-dependent apoptosis. Its developmental role is unexpectedly dispensable: loss of EDAR or of ectodysplasin itself causes hypohidrotic ectodermal dysplasia, but Eda2r-null mice have essentially normal hair, teeth and glands.

What EDA2R is actually known for now is p53. It was identified by cross-referencing p53-introduced cells against tumour tissue, and p53 drives it through two response elements in intron 1 — so this is a direct target, not an inferred one. In colorectal cancer the gene is silenced by promoter hypermethylation at high frequency, and loss of it increases cell adhesion and spreading and confers resistance to p53-induced apoptosis, which is the basis of the proposal that it mediates a p53-regulated anoikis pathway. Independent work confirmed p53-dependent transactivation across several cell types and tissues in vivo, including during chemotherapy-induced hair loss, though EDA2R is not required for that hair loss.

A separate literature has grown recently. EDA2R is among the most consistently age-upregulated transcripts across human and animal tissues, and it is elevated in denervated muscle, cancer cachexia and muscular dystrophy. The mechanism is worked out best in cachexia: EDA-A2 acting on EDA2R activates NIK and the non-canonical NF-κB pathway to atrophy myotubes, tumour-derived oncostatin M raises muscle EDA2R, and deleting either EDA2R or muscle NIK protects tumour-bearing mice from losing muscle mass. The extension of that account to ordinary ageing muscle is so far mostly associational.

## What is uncertain

The direct-versus-indirect question is settled for the transcription, but whether the protein does anything in these cells is genuinely open: no ligand is supplied in this experiment, EDA-A2 is not appreciably expressed in most cancer lines, and the apoptosis-inducing activity rests largely on overexpression. Induction here may be transcription without signalling. The receptor biology is thin overall — far thinner than the p53-target literature that cites it. The low baseline that makes the fold-change large also makes single-cell detection sparse and ratios unstable. Being X-linked, its dosage may vary with donor sex and X-inactivation state across the pooled lines, a source of between-line variance unrelated to p53. The cachexia work is mouse genetics in muscle and says nothing about these lines; the ageing arm of that literature is young and largely associational.

## References

- Yan et al., 2000, Science — identified XEDAR/EDA2R as the receptor for the EDA-A2 isoform and showed a two-amino-acid switch in ectodysplasin selects between the two receptors.
- Tanikawa et al., 2009, Oncogene — identified XEDAR as a p53 target driven by two response elements in intron 1, frequently hypermethylated in colorectal cancer, and proposed it mediates p53-regulated anoikis.
- Brosh et al., 2010, FEBS Letters — showed p53-dependent transactivation of EDA2R across cell types and tissues, including in chemotherapy-induced hair loss, which nonetheless does not require EDA2R.
- Bilgic et al., 2023, Nature — showed EDA2R–NIK signalling drives muscle atrophy in cancer cachexia, with loss of EDA2R or of muscle NIK protecting tumour-bearing mice.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.42× (z +9.3, q 6e-18, up in 0 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.82× (z +8.7, q 7e-16, up in 12 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.540× (z -6.5, q 3e-08, down in 12 of 19 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTCHD4]] (+0.81, fdr 7e-06), [[ZMAT3]] (+0.79, fdr 7e-06), [[FDXR]] (+0.79, fdr 7e-06); moves opposite to [[FARP2]] (-0.42, fdr 2e-04).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 27 go from it, the strongest it → [[ZMAT3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5167.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.42×** | +9.3 | 6e-18 | 0/12 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.82×** | +8.7 | 7e-16 | 12/19 (NCI-H460, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +7.5 | 1e-11 | 8/10 (NCI-H460, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +6.3 | 3e-08 | 10/19 (A498, NCI-H460, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.73×** | +5.5 | 3e-06 | 4/13 (A498, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.66×** | +5.3 | 9e-06 | 10/18 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +5.2 | 2e-05 | 0/11 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.60×** | +5.0 | 5e-05 | 10/18 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.65×** | +4.9 | 7e-05 | 9/17 (A-172, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +4.9 | 7e-05 | 7/15 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.85×** | +4.6 | 2e-04 | 0/12 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +4.6 | 2e-04 | 7/18 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.35×** | +4.4 | 6e-04 | 7/19 (NCI-H460, A498, …) | top dose only |  |
| [[Imiquimod (maleate) (drug)]] 5 µM |  | **1.52×** | +4.2 | 0.001 | 0/18 | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.001 | 3/17 (C32, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.71×** | +4.0 | 0.002 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +3.6 | 0.010 | 7/18 (A549, A498, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.021 | 8/18 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.57×** | +3.4 | 0.021 | 1/15 (SK-MEL-2) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.38×** | +3.4 | 0.021 | 9/19 (NCI-H460, A549, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.035 | 6/18 (NCI-H460, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5167.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.540×** | -6.5 | 3e-08 | 12/19 (A549, A498, …) | top dose only | cell-cycle shift (explains ~23% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.552×** | -6.3 | 7e-08 | 14/18 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.572×** | -5.9 | 6e-07 | 13/19 (A498, H4, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.684×** | -3.9 | 0.014 | 9/18 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.705×** | -3.7 | 0.022 | 10/19 (CHP-212, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.723×** | -3.5 | 0.052 | 8/18 (NCI-H2347, A498, …) | inconsistent across doses |  |
| [[Isocorydine (drug)]] 5 µM |  | **0.799×** | -3.4 | 0.062 | 1/19 (SHP-77) | top dose only | position effect removed |
| [[Ribociclib (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.748× | -3.1 | 0.14 | 0/18 | inconsistent across doses | position effect removed |
| [[Hydroxyurea (drug)]] 0.5 µM |  | 0.751× | -3.1 | 0.14 | 0/18 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5167. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 37.8 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.178× (z -13.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.242× (z -11.4) |
| [[A549 (line)]] | wt | 39.9 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.153× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 39.4 | 1 | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.53× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.258× (z -9.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.290× (z -8.7) |
| [[A-172 (line)]] | wt | 28.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.170× (z -9.7) |
| [[A-427 (line)]] | wt | 16.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -9.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[H4 (line)]] | wt | 39.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0678× (z -13.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HepG2_C3A (line)]] | wt | 11.8 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0607× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 30.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.128× (z -10.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[LOX-IMVI (line)]] | wt | 22.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.212× (z -9.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 8.15 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0853× (z -9.4) |
| [[AN3 CA (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.538 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.681 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.485 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.588 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.536 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.601 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.857 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.475 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.611 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.801 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.498 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.588 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.676 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.791 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.828 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.757 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.783 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5167), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTCHD4]] | +0.81 | +0.66 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[ZMAT3]] | +0.79 | +0.62 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[FDXR]] | +0.79 | +0.72 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[RRM2B]] | +0.77 | +0.62 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[MDM2]] | +0.76 | +0.59 / +0.78 | both halves | 7e-06 |  |
| [[PINCR]] | +0.75 | +0.53 / +0.78 | both halves | 1e-05 | **novel candidate** |
| [[ACTA2]] | +0.73 | +0.57 / +0.75 | both halves | 9e-06 |  |
| [[GRIN2C]] | +0.73 | +0.54 / +0.72 | both halves | 1e-05 | **novel candidate** |
| [[SPATA18]] | +0.72 | +0.35 / +0.77 | both halves | 1e-04 |  |
| [[BAX]] | +0.71 | +0.46 / +0.71 | both halves | 3e-05 |  |
| [[PURPL]] | +0.70 | +0.37 / +0.77 | both halves | 7e-05 |  |
| [[DCP1B]] | +0.69 | +0.54 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FARP2]] | -0.42 | -0.32 / -0.42 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EDA2R's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GRIN2C]] | B | GRIN2C activity raises EDA2R's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 2.56× lower at baseline in the lines without GRIN2C | 0.036 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |
| [[CYFIP2]] | B | CYFIP2 activity raises EDA2R's level | lines that do not express CYFIP2 (9) vs lines expressing it (41) | 2.46× lower at baseline in the lines without CYFIP2 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000226965, GRIN2C, SEMA6A |
| [[HDAC6]] | B | HDAC6 activity raises EDA2R's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PINCR]] | C | PINCR activity raises EDA2R's level | lines that do not express PINCR (29) vs lines expressing it (21) | 3.62× lower at baseline in the lines without PINCR | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; co-absent with the target |
| [[DDX3Y]] | C | DDX3Y activity raises EDA2R's level | lines that do not express DDX3Y (30) vs lines expressing it (20) | 2.79× lower at baseline in the lines without DDX3Y | 0.013 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P; co-absent with the target |
| [[PTCHD4]] | C | PTCHD4 activity raises EDA2R's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 4.50× lower at baseline in the lines without PTCHD4 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1; co-absent with the target |
| [[NLGN4Y]] | C | NLGN4Y activity raises EDA2R's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 3.28× lower at baseline in the lines without NLGN4Y | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |
| [[PRKY]] | C | PRKY activity raises EDA2R's level | lines that do not express PRKY (30) vs lines expressing it (20) | 2.77× lower at baseline in the lines without PRKY | 0.039 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ZFY, KDM5D, RPS4Y1; co-absent with the target |
| [[TP53]] | C | TP53 activity raises EDA2R's level | recorded loss-of-function mutation of TP53 in 33 lines vs 17 not recorded | 3.78× lower at baseline in the TP53-altered lines | 0.533 over the table, 0.014 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 25, C 2. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZMAT3]] | B | EDA2R activity raises ZMAT3's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 2.63× lower at baseline in the lines without EDA2R | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[MIR3659HG]] | B | EDA2R activity raises MIR3659HG's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.34× lower at baseline in the lines without EDA2R | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[ACTA2]] | B | EDA2R activity raises ACTA2's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.91× lower at baseline in the lines without EDA2R | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[FBXO22]] | B | EDA2R activity raises FBXO22's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.33× lower at baseline in the lines without EDA2R | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[FDXR]] | B | EDA2R activity raises FDXR's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.93× lower at baseline in the lines without EDA2R | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[AEN]] | B | EDA2R activity raises AEN's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.74× lower at baseline in the lines without EDA2R | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[ZNF79]] | B | EDA2R activity raises ZNF79's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.32× lower at baseline in the lines without EDA2R | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[NOPCHAP1]] | B | EDA2R activity raises NOPCHAP1's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.27× lower at baseline in the lines without EDA2R | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[TRIAP1]] | B | EDA2R activity raises TRIAP1's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.30× lower at baseline in the lines without EDA2R | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[GRIN2C]] | B | EDA2R activity raises GRIN2C's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 2.00× lower at baseline in the lines without EDA2R | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[BLOC1S2]] | B | EDA2R activity raises BLOC1S2's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.36× lower at baseline in the lines without EDA2R | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[CYFIP2]] | B | EDA2R activity raises CYFIP2's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.78× lower at baseline in the lines without EDA2R | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.830). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.1, 36.5); signed map (42.5, -24.1). **Vector** length 59.4, 17.0% of its response variance represented; |z| ≥ 3 in 538 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *p53 pathway* (hallmark, mean cos +0.57 to 26); *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.61 to 6); *apoptosis* (hallmark, mean cos +0.60 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +7.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.6 | +8.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.6 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +9.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +6.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.9 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | -0.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +4.9 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.0 | -6.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.9 | -5.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.8 | -6.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.2 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -3.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.9 | +1.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -1.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | ectodysplasin A2 receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq12 — chrX:66,595,637-66,639,298 (-) |
| Ensembl biotype | protein_coding |
| Also known as | XEDAR, EDA-A2R, EDAA2R, TNFRSF27 |
| Gene groups (HGNC) | Tumor necrosis factor receptor superfamily |
| Reactome | 3 pathways, smallest: TNFs bind their physiological receptors; TNFR2 non-canonical NF-kB pathway; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAV5](https://www.uniprot.org/uniprotkb/Q9HAV5) (Tumor necrosis factor receptor superfamily member 27):

> Receptor for EDA isoform A2, but not for EDA isoform A1. Mediates the activation of the NF-kappa-B and JNK pathways. Activation seems to be mediated by binding to TRAF3 and TRAF6.

**Summary**, from NCBI Gene [60401](https://www.ncbi.nlm.nih.gov/gene/60401):

> The protein encoded by this gene is a type III transmembrane protein of the TNFR (tumor necrosis factor receptor) superfamily, and contains cysteine-rich repeats and a single transmembrane domain. This protein binds to the EDA-A2 isoform of ectodysplasin, which plays an important role in maintenance of hair and teeth. Alternatively spliced transcript variants encodes distinct protein isoforms. [provided by RefSeq, Apr 2016]

**Accessions** — [HGNC:17756](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17756) · Entrez [60401](https://www.ncbi.nlm.nih.gov/gene/60401) · UniProt [Q9HAV5](https://www.uniprot.org/uniprotkb/Q9HAV5) · Ensembl [ENSG00000131080](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131080)

## Data

Gene col 5167: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5167); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5167, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5167]; `tensor/DDL_lfc|DDL_z.npy` [5167]; `embed/gene_vectors.npy` [5167]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5167 or target_col == 5167). Every well: [[EDA2R — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/EDA2R.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
